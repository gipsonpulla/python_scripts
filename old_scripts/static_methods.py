#!/usr/bin/python3
#static methonds
from datetime import datetime

class Calender:
    def __init__(self):
        self.events = []
    
    def add_event(self, event_name):
        self.events.append(event_name)

    def display_events(self):
        print (f"Events = {self.events}")

    @staticmethod
    def is_weekend(date: datetime):
        if date.weekday() > 4:
            print (f"weekend")
        else:
            print (f"weekday")

obj1 = Calender()

obj1.add_event("DSA")
obj1.add_event("Party")
obj1.add_event("Coding")
obj1.display_events()
current_date = datetime.now()
Calender.is_weekend(current_date)

