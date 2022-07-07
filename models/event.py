class Event():
    def __init__(self, date, _event_name, _num_of_guests, _room_location, _description, _event_recurring):
        self.date = date
        self.event_name = _event_name
        self.num_of_guests = _num_of_guests
        self.room_location = _room_location
        self.description = _description
        self.event_recurring = _event_recurring