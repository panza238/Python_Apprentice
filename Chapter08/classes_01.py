"""Module to explore and explain Python classes"""


class Flight(object):
    """Flight class. Defines flight routes."""
    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError("No airline code in '{}'".format(number))
            # If I raise an Exception in __init__, the object is not created (it's not instantiated)
        if not number[:2].isupper():
            raise ValueError("Invalid airline code '{}'".format(number))
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError("Invalid route number '{}'".format(number))
        self._number = number
        self._aircraft = aircraft

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        # by doing this, the user only has to interact with ONE object, the flight object.
        return self._aircraft.model()


class Aircraft(object):
    """Aircraft object"""
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1),
                "ABCDEFGHJK"[:self._num_seats_per_row])


a = Aircraft("G-EUPT", "Airbus A319", num_rows=22, num_seats_per_row=6)
f = Flight("AA1425", a)
