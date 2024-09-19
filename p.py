from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:your_password@localhost/fitness_center_db'
db = SQLAlchemy(app)

class Member(db.Model):
    def __init__(self, Name, Age, Genger, Weight, Active=True):
        self.Name = Name
        self.Age = Age
        self.Gender = Gender
        self.Weight = Weight
        self.Active = Active


    def display_info(self):
        print(f"Name: {self.Name}")
        print(f"Age: {self.Age}")
        print(f"Gender: {self.Gender}")
        print(f"Weight: {self.Weight}")
        print(f"Active: {'Active' if self.Active else 'Not Active'}")

def update_member_name(self, new_Name):
    self.Name= new_Name


class WorkoutSession(db.Model):
    def __init__(self, session_id, member_id, session_date, session_time, Session_type):
        self.session_id = session_id
        self.member_id = member_id
        self.session_date = session_date
        self.session_time = session_time
        self.Session_type = Session_type


    def display_info(self):
        print(f"session_id: {self.session_id}")
        print(f"member_id: {self.member_id}")
        print(f"session_date: {self.session_date}")
        print(f"session_time: {self.session_time}")
        print(f"Session_type: {self.Session_type}")

def update_Session_type(self, new_Session_type):
    self.Session_type= new_Session_type

    while True:
        print("\nWelcome to the Workout Management System!")
        print("Main Menu:")
        print("1. Member/Membership Operations")
        print("2. Workout Operations")
        print("3. Quit")

        choice = input("Enter your choice: ")
        if choice == '1':
                print("Welcome to the member operations menue")
                print("1. If you would like to add a new member") 
                print("2. If you would like to remove a member")
                print("3. If you would like to display member information")
                print("4. If you would like to update the member name")
                    if select =='1':
                        print("We are going to all a new member")
                            name = input("input Name")
                            Age = input("input Age")
                            Gender = input("input Gender")
                            weight = input("input weight")
                            Active = bool(input("True or False"))
                            member1 = Member(Name, Age, Gender, Weight, Active)
                            print(member1)
                    elif select =='2':
                        mr = input("Workout session you would like to delete")
                        mr.delete()
                    elif select =='3':
                        print("display membership information")
                        a = input("input the name of the member you would like to view")
                        print(a)
                    elif select == '4':
                        z = input("input new customer name")
                        self.update_member_name(z)
                    else:
                         print("please select a valid key")
        elif choice == '2':
                choice = input("Enter your choice: "CRUD)
            if choice == '1':
                print("Welcome to the Workout operations menue")
                print("1. If you would like to add a new workout session") 
                print("2. If you would like to remove a workout session")
                print("3.if you would like to display workout session information")
                print("4. if you would like to update a piece of the workout session")
                    if select =='1':
                        print("We are going to add a workpout session")
                        session_id = input("input session_id")
                        member_id = input("input member_id")
                        session_date = input("input session_date")
                        session_time = input("input session_time")
                        Session_type = input("input Session_type")
                        Workout1 = Workout(session_id, member_id, session_date, session_time, Session_type)
                    print(member1)
                    elif select =='2':
                        print("we are going to remove a workout session")
                            ws = input("Workout session you would like to delete")
                            ws.delete()
                    elif select =='3':
                        print("we are going to display workout session")
                        i = input("input the workout session you want to display")
                        print(i)
                    elif select =='4':
                        print("we are going to update a workout session")
                         g = input("input new workout activity/ new session_type")
                         self.update_Session_type(g)
                    else:
                         print("please select a valid key")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
