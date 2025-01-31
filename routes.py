#This blueprint file is created as a subset of all the flask endpoints with their own configuration settings
#It keeps the flask endpoints with their own configuration settings so that they can be easily modified or new endpoints can be added
#Blueprints can be imported to the main app as a library, much like how base html files are 'extended' into other html files 
#There can be multiple blueprints for different sets of endpoints with their own configuration settings
#In a gist, a blueprint is like a collection of endpoints with their own configuration settings and ready to be used in the main flask app without having to constantly adjusting the settings if all the endpoints were in a single file

from flask import Blueprint, render_template, request, redirect, url_for, current_app
#'defaultdict' is a dictionary which creates a default value for when a user tries to access a non-existent value 
#from collections import defaultdict
import datetime

import uuid

#"habits" is the blueprint name; template_folder and static_folder keyword arguments must be provided for the bluprint to have access to them
#Note: Remember to add the "static_folder" argument in the app.py as well, with the same folder name as in the blueprint
pages = Blueprint("habits", __name__, template_folder="Templates", static_folder="pretty_stuff")

#habits = ["Workout (test data)"]

#completions = defaultdict(list)

#This context processor will make the date_range function available to all the rendered templates via the dictionary it returns;
#By default, the context processor function (add_cal_date_range()) accepts a dictionary, so it'll return a dictionary as it's final value
@pages.context_processor
def add_cal_date_range():
    def date_range(start: datetime.datetime):
        #timedelta() adds or subtracts dates from the given date value
        dates = [start + datetime.timedelta(days=diff) for diff in range(-3,4)]
        return dates
    return{"date_range":date_range}

def today_at_midnight():
    today = datetime.datetime.today()
    #By default, hr, min and sec are 0, so this function returns the date at midnight
    return datetime.datetime(today.year, today.month, today.day) 

@pages.route("/")
def index():
    #retreives date value in string format from the url's query string parameter; the url will have different date values depending upon the date links we click on
    date_str = request.args.get("date")
    if date_str:
        #When a date is passed in as a string, it is converted to iso format; here we convert the date from iso format to a date object
        selected_date = datetime.datetime.fromisoformat(date_str)

    else:
        selected_date = today_at_midnight()

    #fetching all the habits added upto the currently selected date
    habits_on_date = current_app.db.habits.find({"added":{"$lte":selected_date}})

    completions = [
        #The "habits" is used to retrieve the habitID from the completions collection
        habit["habit"]
        for habit in current_app.db.completions.find({"date":selected_date})
    ]

    return render_template(
        "index.html",
        habits=habits_on_date, 
        title = "Habit Tracker -- Home",
        selected_date = selected_date,
        completions = completions
        )

@pages.route("/add",methods = ["GET","POST"])
def addHabit():
    today = today_at_midnight()

    if request.method == "POST":

        #When we insert data into a mongodb collection that doesn't exist, MongoDB will create a collection of that specified name and store data in it
        current_app.db.habits.insert_one({

            #uuid will generate a unique id of long-string numbers or letters
            "_id": uuid.uuid4().hex, "added":today, "name": request.form.get("habit")
        })
        

    return render_template(
        "AddHabit.html",
        title = "Habit Tracker -- Add habit",
        selected_date = today)

@pages.route("/complete", methods = ["POST"])
def complete():
    date_string = request.form.get("date")
    habit = request.form.get("habitID")
    date = datetime.datetime.fromisoformat(date_string)

    current_app.db.completions.insert_one({"date":date, "habit":habit})

    #adding the habit value to the currently selected date key; since this is a default dictionary, we don't need to have the date key added prior to adding the habit 
    #completions[date].append(habit)

    #We use "habits.index" because we're accessing index as a subroute of habits blueprint; alternatively, we can also use ".index" which will refer to the index subroute within the current blueprint, which is "habits"
    return redirect(url_for("habits.index",date = date_string))



