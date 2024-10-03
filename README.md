Module 6 Lesson 3: Assignments | Introduction to Object-relational Mappers (ORM)
Remember to take your time and work through each question diligently! Test your code, make sure it works, and try to find ways to improve. Once you are happy and satisfied with your code, upload it to Github, then turn in your Github link at the bottom of the page!

Don't forget. Make sure this assignment is in it's own repository. Not mixed in with others!
Flask-SQLAlchemy Fitness Center Management

Objective: The aim of this assignment is to transition from a traditional SQL approach to using Flask-SQLAlchemy for managing a fitness center's database. This assignment will enhance your skills in ORM (Object-Relational Mapping), specifically with Flask-SQLAlchemy, to build RESTful APIs for handling database operations with `Members` and `WorkoutSessions` tables.

Task 1: Setting Up Flask with Flask-SQLAlchemy - Initialize a new Flask project and set up a virtual environment. - Install Flask, Flask-SQLAlchemy, and Flask-Marshmallow. - Configure Flask-SQLAlchemy to connect to your database. - Define `Members` and `WorkoutSessions` models using Flask-SQLAlchemy ORM.

Expected Outcome: A Flask project connected to a database using SQLAlchemy with ORM models for `Members` and `WorkoutSessions`.

Code Example:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/fitness_center_db'
db = SQLAlchemy(app)

class Member(db.Model):
    # Define fields...

class WorkoutSession(db.Model):
    # Define fields...
Task 2: Implementing CRUD Operations for Members Using ORM - Create Flask routes to add, retrieve, update, and delete members using the ORM models. - Apply HTTP methods: POST to add, GET to retrieve, PUT to update, and DELETE to delete members. - Handle errors effectively and return appropriate JSON responses.

Expected Outcome: Functional API endpoints for managing members in the database using Flask-SQLAlchemy, with proper error handling.

Task 3: Managing Workout Sessions with ORM - Develop routes to schedule, update, and view workout sessions using SQLAlchemy. Implement a route to retrieve all workout sessions for a specific member.

Expected Outcome: A comprehensive set of endpoints for scheduling and viewing workout sessions using Flask-SQLAlchemy, with detailed information about each session.
