from managers.abstract_reading_manager import AbstractReadingManager
from managers.pressure_reading_manager import PressureReadingManager
from managers.temperature_reading_manager import TemperatureReadingManager
from readings.abstract_reading import AbstractReading
from readings.pressure_reading import PressureReading
from readings.temperature_reading import TemperatureReading
from flask import Flask, session, redirect, url_for, escape, request
import json
from collections import namedtuple

app = Flask(__name__)


@app.route('/sensor/<string:sensor_type>/reading', methods=['POST'])
def add_reading(sensor_type):
    """creates reading object"""
    reading = request.get_json()
    print(reading)
    print(json_to_list(reading))
    sensor_input = json_to_list(reading)
    if sensor_type == "temperature":
        sensor = TemperatureReadingManager("data/temperature_results.csv")
        temp_read = TemperatureReading(*sensor_input)
        print(temp_read.get_timestamp())
        sensor.add_reading(temp_read)
    elif sensor_type == "pressure":
        sensor = TemperatureReadingManager("data/pressure_results2.csv")

    response = app.response_class(
        response=reading,
        status=200,
        mimetype='text/plain'
    )

    return response


def json_to_list(json_dict):
    val_list = []
    for name, val in json_dict.items():
        val_list.append(val)

    return val_list


@app.route('/sensor/<string:sensor_type>/reading/<int:seq_num>', methods=['PUT'])
def update_reading(sensor_type, seq_num):
    """display reading stats of sensor"""
    pass


@app.route('/sensor/<string:sensor_type>/reading/<int:seq_num>', methods=['DELETE'])
def delete_reading(sensor_type, seq_num):
    """display reading stats of sensor"""
    pass


@app.route('/sensor/<string:sensor_type>/reading/<int:seq_num>', methods=['GET'])
def get_reading(sensor_type, seq_num):
    """display reading stats of sensor"""

    pass


@app.route('/sensor/<string:sensor_type>/reading/all', methods=['GET'])
def get_all_readings(sensor_type):
    """display reading stats of sensor"""
    reading = request.get_json()
    print(type(reading))
    pass


# def check_sensor_type(sensor):
#     """checks for sensor type and initializes corresponding sensor object"""
#     if sensor == "temperature":
#         TemperatureReadingManager("temp_results.csv")
#
#
#     elif sensor == "pressure":
#         PressureReadingManager("pressure_results.csv")
#


if __name__ == "__main__":
    app.run()
