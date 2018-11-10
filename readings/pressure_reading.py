from readings.abstract_reading import AbstractReading


class PressureReading(AbstractReading):
    """ Concrete Implementation of a Pressure Reading """

    # CONSTANTS
    HIGH_PRESS_ERROR = "HIGH_PRESSURE"
    LOW_PRESS_ERROR = "LOW_PRESSURE"
    STATUS_GOOD = "GOOD"

    def __init__(self, date, sensor_name, seq_num, lowest_temp, avg_temp, highest_temp, status):
        """ Temperature Reading Constructor """

        super().__init__(date, seq_num, sensor_name, lowest_temp, avg_temp, highest_temp, status)

    def is_error(self):
        """ Returns True if there's a there's an error and False if there's no error """
        if self._status != self.STATUS_GOOD:
            return True

        return False

    def get_error_msg(self):
        """ Returns the error message (or None if not an error) """
        status_display = None

        reading_display_datetime = self._timestamp.strftime('%Y/%m/%d %H:%M')

        reading_seq_num = self._sequence_num

        if self._status == self.HIGH_PRESS_ERROR:
            status_display = "High Pressure (100 kPA) at %s, Sequence: %d" % (reading_display_datetime, reading_seq_num)
        elif self._status == self.LOW_PRESS_ERROR:
            status_display = "Low Pressure (0 kPA) at %s, Sequence: %d" % (reading_display_datetime, reading_seq_num)

        return status_display
