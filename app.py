from flask import Flask, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from models import Crop, Wine, Preserve
from config import Config

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object(Config())
db.init_app(app)
migrate = Migrate(app, db)

from functions import update_data, build_crop_list, find_net_values


@app.route('/display')
def display():  # put application's code here
    crop_list = build_crop_list()

    selected_crop_id = request.args.get("crops")

    if selected_crop_id:
        net_values = find_net_values(int(selected_crop_id))

        data = {
            "cropBase": net_values["crop_values"][0],
            "cropSilver": net_values["crop_values"][1],
            "cropGold": net_values["crop_values"][2],
            "cropIridium": net_values["crop_values"][3],
            "wineBase": net_values["wine_values"][0],
            "wineSilver": net_values["wine_values"][1],
            "wineGold": net_values["wine_values"][2],
            "wineIridium": net_values["wine_values"][3],
            "preserveBase": net_values["preserve_values"][0],
            "preserveSilver": net_values["preserve_values"][1],
            "preserveGold": net_values["preserve_values"][2],
            "preserveIridium": net_values["preserve_values"][3]
        }
    else:
        data = {}

    variables = {
        "data": data,
        "crop_list": crop_list
    }
    return render_template("stardew-graph-viewer.html", **variables)


@app.route("/insert")
def insert():
    submit_pressed = request.args.get("submission")
    if submit_pressed:
        update_data(request.args.get("crop-name"))

    return render_template("stardew-data-insertion.html")


if __name__ == '__main__':
    app.run()
