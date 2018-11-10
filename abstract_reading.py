import datetime
class AbstractReading:
    """ Temperature Sensor Reading """

    def __init__(self, date, seq_num, sensor_name, lowest_temp, avg_temp, highest_temp, status):
        """ Initializes the sensor reading """
        self._timestamp = date
        self._sensor_model = sensor_name
        self._sequence_num = seq_num
        self._min = lowest_temp
        self._avg = avg_temp
        self._max = highest_temp
        self._status = status

    def get_timestamp(self):
        """ Getter for timestamp """
        return self._timestamp

    def get_sensor_model(self):
        """ Getter for sensor model """
        return self._sensor_model

    def get_sequence_num(self):
        """ Getter for sequence number """
        return self._sequence_num

    def set_sequence_num(self, sequence_num):
        """ Setter for sequence number"""
        self._sequence_num = sequence_num

    def get_min_value(self):
        """ Getter for the minimum temperature """
        return self._min

    def get_avg_value(self):
        """ Getter for the average temperature """
        return self._avg

    def get_max_value(self):
        """ Getter for the maximum temperature """
        return self._max

    def get_range(self):
        """ Getter for the temperature range """
        return self._max - self._min

    def get_status(self):
        """ getter for status"""
        return self._status

    def is_error(self):
        """ Abstract Method - Is Reading and Error """
        raise NotImplementedError("Must be implemented")

    def get_error_msg(self):
        """ Abstract Method - Get Error Readings """
        raise NotImplementedError("Must be implemented")
