import threading

from flask import Flask, jsonify, request

from Water_counter import Water_counter, go_count

app = Flask(__name__)


@app.route('/api/v1/water', methods=['GET'])
def get_water():
    return jsonify({'hot': Water_counter.hot,
                    'cold': Water_counter.cold})


@app.route('/api/v1/water', methods=['POST'])
def set_water():
    req = request.get_json()
    Water_counter.hot = req["hot"]
    Water_counter.cold = req["cold"]
    return jsonify({'water_update': True})


if __name__ == "__main__":
    threading.Thread(target=lambda: app.run(debug=True, use_reloader=False)).start()
go_count()
