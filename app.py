from flask import Flask, jsonify, request
import csv

app = Flask(__name__)


def load_assets():
    assets = []

    with open('assets.csv', mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            assets.append(row)

    return assets


@app.route('/assets', methods=['GET'])
def get_assets():
    assets = load_assets()
    return jsonify(assets)


@app.route('/assets/search', methods=['GET'])
def search_assets():
    assets = load_assets()

    status = request.args.get('status')
    asset_type = request.args.get('type')

    filtered_assets = assets

    if status:
        filtered_assets = [
            asset for asset in filtered_assets
            if asset['status'].lower() == status.lower()
        ]

    if asset_type:
        filtered_assets = [
            asset for asset in filtered_assets
            if asset['asset_type'].lower() == asset_type.lower()
        ]

    return jsonify(filtered_assets)


@app.route('/summary', methods=['GET'])
def asset_summary():
    assets = load_assets()

    total_assets = len(assets)

    assigned = len([
        asset for asset in assets
        if asset['status'] == 'Assigned'
    ])

    available = len([
        asset for asset in assets
        if asset['status'] == 'Available'
    ])

    maintenance = len([
        asset for asset in assets
        if asset['status'] == 'Maintenance'
    ])

    summary = {
        'total_assets': total_assets,
        'assigned': assigned,
        'available': available,
        'maintenance': maintenance
    }

    return jsonify(summary)


if __name__ == '__main__':
    app.run(debug=True)
