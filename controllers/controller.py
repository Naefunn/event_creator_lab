from flask import render_template, request, redirect
from app import app
from models.event_list import add_new_event, fringe_events #create object
from models.event import Event
from datetime import date

@app.route('/events')
def index():
    return render_template('index.html', fringe_events = fringe_events)

@app.route('/events', methods = ['POST'])
def add_event():
    event_date = request.form['input_show_date']
    event_name = request.form['input_show_name']
    event_num_of_guests = request.form['input_show_capacity']
    event_location = request.form['input_show_room_location']
    event_description = request.form['input_show_description']
    event_recurring = request.form['input_recurring_event']
    new_event = Event(event_date, event_name, event_num_of_guests, event_location, event_description, event_recurring==False)
    print(new_event)
    add_new_event(new_event)
    return redirect('/events')

