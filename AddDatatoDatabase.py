import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facerecognitionattendanc-eb678-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "963852":
        {
            "name": "Elon Musk",
            "major": "Robotics",
            "starting_year": 2000,
            "total_attendance": 0,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2024-08-31 00:20:48"
        },
    "125135":
        {
            "name": "Usain bolt",
            "major": "Athelete",
            "starting_year": 2016,
            "total_attendance": 55,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2024-08-31 00:20:48"
        },
    "123654":
        {
            "name": "Sathya",
            "major": "Traveller",
            "starting_year": 2022,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2024-08-31 00:20:48"
        }
}

print("Sucessfully added")

for key, value in data.items():
    ref.child(key).set(value)