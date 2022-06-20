from flask import request
from app import db
from models import Crop


def update_data(crop_name: str):
    crop = Crop.query.filter_by(name=crop_name).first()
    if crop:
        crop.seed_cost = request.args.get("seed-cost")
        crop.maturation_days = request.args.get("maturation-days")
        crop.base_value = request.args.get("crop-base")
        crop.silver_value = request.args.get("crop-silver")
        crop.gold_value = request.args.get("crop-gold")
        crop.iridium_value = request.args.get("crop-iridium")
        crop.wine_value = request.args.get("wine-base")
        crop.silver_wine_value = request.args.get("wine-silver")
        crop.gold_wine_value = request.args.get("wine-gold")
        crop.iridium_wine_value = request.args.get("wine-iridium")
        crop.wine_production_days = request.args.get("wine-production")
        crop.preserve_value = request.args.get("preserve-base")
        crop.silver_preserve_value = request.args.get("preserve-silver")
        crop.gold_preserve_value = request.args.get("preserve-gold")
        crop.iridium_preserve_value = request.args.get("preserve-iridium")
        crop.preserve_production_days = request.args.get("preserve-production")

    else:
        new_crop = Crop(
            name=request.args.get("crop-name"),
            seed_cost=request.args.get("seed-cost"),
            maturation_days=request.args.get("maturation-days"),
            base_value=request.args.get("crop-base"),
            silver_value=request.args.get("crop-silver"),
            gold_value=request.args.get("crop-gold"),
            iridium_value=request.args.get("crop-iridium"),
            wine_value=request.args.get("wine-base"),
            silver_wine_value=request.args.get("wine-silver"),
            gold_wine_value=request.args.get("wine-gold"),
            iridium_wine_value=request.args.get("wine-iridium"),
            wine_production_days=request.args.get("wine-production"),
            preserve_value=request.args.get("preserve-base"),
            silver_preserve_value=request.args.get("preserve-silver"),
            gold_preserve_value=request.args.get("preserve-gold"),
            iridium_preserve_value=request.args.get("preserve-iridium"),
            preserve_production_days=request.args.get("preserve-production")
        )
        db.session.add(new_crop)
        db.session.commit()


def build_crop_list():
    crop_list = []
    all_crops = db.session.query(Crop).all()
    if all_crops:
        for crop in all_crops:
            crop_list.append({
                "crop_name": crop.name,
                "crop_id": crop.id
            })

    return crop_list


def find_net_values(crop_id: int) -> dict:
    selected_crop = Crop.query.filter_by(id=crop_id).first()
    net_crops = collect_net_profits(selected_crop.base_value,
                                    selected_crop.silver_value,
                                    selected_crop.gold_value,
                                    selected_crop.iridium_value)
    net_wines = collect_net_profits(selected_crop.wine_value,
                                    selected_crop.silver_wine_value,
                                    selected_crop.gold_wine_value,
                                    selected_crop.iridium_wine_value)
    net_preserves = collect_net_profits(selected_crop.preserve_value,
                                        selected_crop.silver_preserve_value,
                                        selected_crop.gold_preserve_value,
                                        selected_crop.iridium_preserve_value)

    return {
        "crop_values": net_crops,
        "wine_values": net_wines,
        "preserve_values": net_preserves,
    }


def collect_net_profits(base: int, silver: int, gold: int, iridium: int) -> list:
    # When stacking in the graph, we want gold (for example) to cause the stack to reach gold height, but to by itself
    # only display the profit netted from gold over previous amounts.

    if base:
        silver_net = silver - base
    else:
        silver_net = silver

    if silver:
        gold_net = gold - silver
    elif base:
        gold_net = gold - base
    else:
        gold_net = gold

    if gold:
        iridium_net = iridium - gold
    elif silver:
        iridium_net = iridium - silver
    elif base:
        iridium_net = iridium - base
    else:
        iridium_net = iridium

    return [base, silver_net, gold_net, iridium_net]
