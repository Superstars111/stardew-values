from flask import request
from app import db
from models import Crop, Wine, Preserve


def update_data(crop_name: str):
    crop = Crop.query.filter_by(name=crop_name).first()
    if crop:
        crop.seed_cost = request.args.get("seed-cost")
        crop.maturation_days = request.args.get("maturation-days")
        crop.base_value = request.args.get("crop-base")
        crop.silver_value = request.args.get("crop-silver")
        crop.gold_value = request.args.get("crop-gold")
        crop.iridium_value = request.args.get("crop-iridium")

        wine = Wine.query.filter_by(crop_id=crop.id).first()
        wine.production_days = request.args.get("wine-production")
        wine.base_value = request.args.get("wine-base")
        wine.silver_value = request.args.get("wine-silver")
        wine.gold_value = request.args.get("wine-gold")
        wine.iridium_value = request.args.get("wine-iridium")

        preserve = Preserve.query.filter_by(crop_id=crop.id).first()
        preserve.production_days = request.args.get("preserve-production")
        preserve.base_value = request.args.get("preserve-base")
        preserve.silver_value = request.args.get("preserve-silver")
        preserve.gold_value = request.args.get("preserve-gold")
        preserve.iridium_value = request.args.get("preserve-iridium")

    else:
        new_crop = Crop(
            seed_cost=request.args.get("seed-cost"),
            maturation_days=request.args.get("maturation-days"),
            base_value=request.args.get("crop-base"),
            silver_value=request.args.get("crop-silver"),
            gold_value=request.args.get("crop-gold"),
            iridium_value=request.args.get("crop-iridium")
        )
        new_wine = Wine(
            production_days=request.args.get("wine-production"),
            base_value=request.args.get("wine-base"),
            silver_value=request.args.get("wine-silver"),
            gold_value=request.args.get("wine-gold"),
            iridium_value=request.args.get("wine-iridium")
        )
        new_preserve = Wine(
            production_days=request.args.get("preserve-production"),
            base_value=request.args.get("preserve-base"),
            silver_value=request.args.get("preserve-silver"),
            gold_value=request.args.get("preserve-gold"),
            iridium_value=request.args.get("preserve-iridium")
        )
        db.session.add(new_crop)
        db.session.add(new_wine)
        db.session.add(new_preserve)

        db.session.commit()

        new_crop.wine_id = new_wine.id
        new_crop.preserve_id = new_preserve.id
        new_wine.crop_id = new_crop.id
        new_preserve.crop_id = new_crop.id

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


def find_net_values(crop_id: int) -> dict:
    selected_crop = Crop.query.filter_by(id=crop_id).first()
    selected_wine = Wine.query.filter_by(crop_id=crop_id).first()
    selected_preserve = Preserve.query.filter_by(crop_id=crop_id).first()
    net_crops = collect_net_profits(selected_crop.base_value,
                                    selected_crop.silver_value,
                                    selected_crop.gold_value,
                                    selected_crop.iridium_value)
    net_wines = collect_net_profits(selected_wine.base_value,
                                    selected_wine.silver_value,
                                    selected_wine.gold_value,
                                    selected_wine.iridium_value)
    net_preserves = collect_net_profits(selected_preserve.base_value,
                                        selected_preserve.silver_value,
                                        selected_preserve.gold_value,
                                        selected_preserve.iridium_value)

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
