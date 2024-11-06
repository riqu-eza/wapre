from ..Database.Db import db

class User:
    @staticmethod
    def authenticate(email, password):
        user = db.users.find_one({"email": email, "password": password})
        return user if user else None

    @staticmethod
    def create(Firstname,Secondname,Email, Password,):
        db.users.insert_one({"firstname": Firstname, "password": Password, "secondname": Secondname, "email": Email })

class UploadData:
    def __init__(self, user,date_of_purchase ):
        self.user = user
        self.date_of_purchase = date_of_purchase

    def save(self):
        db.uploads.insert_one({
            "user": self.user,
            "date_of_purchase": self.date_of_purchase
        })
