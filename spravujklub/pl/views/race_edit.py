from flask import request, render_template, redirect
from flask_login import login_required
from main import app, race_controller
from datetime import datetime


@app.route('/race_edit/<race_id>', methods=['GET'])
@login_required
def race_edit(race_id):
    try:
        race = race_controller.get_race_by_id(race_id)
    except Exception as ex:
        print(str(ex))
        return redirect("/")

    name = request.values.get("name")
    date = request.values.get("date")
    deadline = request.values.get("deadline")
    info = request.values.get("info")

    if name is not None and date is not None and deadline is not None and info is not None:
        try:
            # Convert the parameters
            date = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
            deadline = datetime.strptime(deadline, '%Y-%m-%d %H:%M:%S')

            # Update the values
            race.name = name
            race.date = date
            race.deadline = deadline
            race.info = info

            # Commit the session TODO: Solve this to make it somewhere else
            db.session.commit()

            return redirect("/race_detail/%s" % str(race_id))
        except Exception as ex:
            print(str(ex))

    return render_template("race_edit.html", race=race)