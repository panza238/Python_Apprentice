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
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        # by doing this, the user only has to interact with ONE object, the flight object.
        return self._aircraft.model()

    def allocate_seat(self, seat, passenger):
        """Allocate a seat to a passenger.
            Args:
                seat: A seat designator such as '12C' or '21F'.
                passenger: The passenger name.
            Raises:
                ValueError: If the seat is unavailable.
        """
        # row, letter checks
        row, letter = self._parse_seat(seat)
        # Check availability
        if self._seating[row][letter] is not None:
            raise ValueError("Seat {} already occupied".format(seat))
        # Assign
        self._seating[row][letter] = passenger

    def _parse_seat(self, seat):
        """Implementation detail"""
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError("Invalid seat letter {}".format(letter))

        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError("Invalid seat row {}".format(row_text))

        if row not in rows:
            raise ValueError("Invalid row number {}".format(row))

        return row, letter


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

    def num_seats(self):
        rows, row_seats = self.seating_plan()
        return len(rows) * len(row_seats)


class Airbus319(Aircraft):
    """Airbus aircraft"""
    def __init__(self, registration,):
        super().__init__(registration, "Airbus A319", 22, 6)


def make_flight():
    """So that I don't have to create the same element again and again.
    Much more elegant solution than to just declare a and f"""
    f = Flight("BA758", Aircraft("G-EUPT", "Airbus A319",
                                 num_rows=22, num_seats_per_row=6))
    f.allocate_seat('12A', 'Guido van Rossum')
    f.allocate_seat('15F', 'Bjarne Stroustrup')
    f.allocate_seat('15E', 'Anders Hejlsberg')
    f.allocate_seat('1C', 'John McCarthy')
    f.allocate_seat('1D', 'Richard Hickey')

    g = Flight("AA217", Airbus319("G-PANZ"))
    g.allocate_seat('1A', 'Panza')
    g.allocate_seat('2A', 'Residente')

    return f, g
