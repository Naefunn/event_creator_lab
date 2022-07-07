from models.event import *
from datetime import date

event1 = Event(date(2022,7,9), "Bad Comedy 1", 10, "dark basement", "Really bad fringe comedy in a dark basement bar", True)
event2 = Event(date(2022,7,10), "Bad Comedy 2", 7, "dark room", "Another bad comedy, this time in a room", False)

fringe_events = [event1, event2]

def add_new_event(event):
    fringe_events.append(event)

