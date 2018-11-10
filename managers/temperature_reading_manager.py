from managers.abstract_reading_manager import AbstractReadingManager
from readings.temperature_reading import TemperatureReading
import datetime


class TemperatureReadingManager(AbstractReadingManager):
    # CONSTANTS
    DATETIME_INDEX = 0
    SEQ_NUM_INDEX = 1
    SENSOR_NAME_INDEX = 2
    LOW_INDEX = 3
    AVG_INDEX = 4
    HIGH_INDEX = 5
    STATUS_INDEX = 6

    def _load_reading_row(self, row):
        """ Loads list into a TemperatureReading object """
        print("row is" , row)
        reading_datetime = datetime.datetime.strptime(row[TemperatureReadingManager.DATETIME_INDEX],
                                                      "%Y-%m-%d %H:%M:%S.%f")

        temp_reading = TemperatureReading(reading_datetime,
                                          int(row[TemperatureReadingManager.SEQ_NUM_INDEX]),
                                          row[TemperatureReadingManager.SENSOR_NAME_INDEX],
                                          float(row[TemperatureReadingManager.LOW_INDEX]),
                                          float(row[TemperatureReadingManager.AVG_INDEX]),
                                          float(row[TemperatureReadingManager.HIGH_INDEX]),
                                          row[TemperatureReadingManager.STATUS_INDEX])
        print("temp reading is", temp_reading)
        return temp_reading

    def _write_reading_row(self, temp_reading):
        """formats a row in the csv file for a reading"""

        temp_reading_list = [temp_reading.get_timestamp().strftime('%Y-%m-%d %H:%M:%S.%f'),
                             temp_reading.get_sequence_num(),
                             temp_reading.get_sensor_model(),
                             temp_reading.get_min_value(),
                             temp_reading.get_avg_value(),
                             temp_reading.get_max_value(),
                             temp_reading.get_status()]

        return temp_reading_list
