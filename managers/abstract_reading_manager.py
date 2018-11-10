# Yuyu Lai A00964939 Assignment2 ACIT2515
import csv


class AbstractReadingManager:
    """maintains abstract readings"""

    def __init__(self, filename):
        """initializes"""
        self._filename = filename
        self._readings = []
        self.newest_seq_num = 0
        self._read_reading_from_file()

    def add_reading(self, reading):
        """appends reading to list of readings"""
        self._readings.append(reading)

        # updates csv file
        self._write_reading_to_file()
        print("reading list has ", self._readings)

    def update_reading(self, reading):
        """updates the reading list with new reading"""
        seq_num = reading.get_seq_num()
        for index, read in self._readings:
            if read.get_sequence_number() == seq_num:
                self._readings[index] = reading

        # updates csv file
        self._write_reading_to_file()



    def delete_reading(self, seq_num):
        """deletes reading based on sequence number"""
        for reading in self._readings:
            if reading.get_seq_num() == seq_num:
                self._readings.remove(reading)

        # updates csv file
        self._write_reading_to_file()

    def get_reading(self, seq_num):
        """get reading according to sequence number"""
        for reading in self._readings:
            if reading.get_seq_num() == seq_num:
                return reading

    def get_all_readings(self):
        """get all readings in reading list"""
        return self._readings

    def _read_reading_from_file(self):
        """read each row in csv"""
        with open(self._filename) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                row_reading = self._load_reading_row(row)
                # self.add_reading(row_reading)
                self._readings.append(row_reading)

    def _write_reading_to_file(self):
        """write reading to csv file"""
        my_file = open(self._filename, 'w', newline='')
        with my_file:
            writer = csv.writer(my_file)
            for reading in self._readings:
                write_list = self._write_reading_row(reading)
                writer.writerow(write_list)

    def _load_reading_row(self, row):
        """ Abstract Method - Returns a new sensor reading """
        raise NotImplementedError("Must be implemented")

    def _write_reading_row(self, reading):
        """ Abstract Method - Returns a new sensor reading """
        raise NotImplementedError("Must be implemented")
