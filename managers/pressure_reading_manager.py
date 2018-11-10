from managers.abstract_reading_manager import AbstractReadingManager
from readings.pressure_reading import PressureReading
import datetime


class PressureReadingManager(AbstractReadingManager):
    # CONSTANTS
    DATETIME_INDEX = 0
    SENSOR_NAME_INDEX = 1
    SEQ_NUM_INDEX = 2
    LOW_INDEX = 3
    AVG_INDEX = 4
    HIGH_INDEX = 5
    STATUS_INDEX = 6

    def _load_reading_row(self, row):
        """ Loads list into a PressureReading object """

        reading_datetime = datetime.datetime.strptime(row[PressureReadingManager.DATETIME_INDEX], "%Y-%m-%d %H:%M")

        pressure_reading = PressureReading(reading_datetime,
                                           row[PressureReadingManager.SENSOR_NAME_INDEX],
                                           int(row[PressureReadingManager.SEQ_NUM_INDEX]),
                                           float(row[PressureReadingManager.LOW_INDEX]),
                                           float(row[PressureReadingManager.AVG_INDEX]),
                                           float(row[PressureReadingManager.HIGH_INDEX]),
                                           row[PressureReadingManager.STATUS_INDEX])

        return pressure_reading

    def _write_reading_row(self, pressure_reading):
        """formats a row in the csv file for a reading"""
        pressure_reading_list = [pressure_reading.get_timestamp().strftime("%Y-%m-%d %H:%M"),
                                 pressure_reading.get_sensor_name(),
                                 pressure_reading.get_sequence_number(),
                                 pressure_reading.get_min_value(),
                                 pressure_reading.get_avg_value(),
                                 pressure_reading.get_max_value(),
                                 pressure_reading.get_status()]

        return pressure_reading_list
