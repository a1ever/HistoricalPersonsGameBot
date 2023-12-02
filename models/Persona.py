import datetime
import random
from enum import StrEnum

DATETIME_MASK = "%d.%m.%Y"


# {
#     "name" : "",
#     "dateOfBirth" : "DD.MM.YYYY",
#     "dateOfDeath" : "DD.MM.YYYY",
#     "nationality" : "",
#     "typeOfActivity" : "",
#     "nameOfPhotoFile" : "",
#     "facts" : [
#       "",
#       ""
#     ]
#   },

class PersonFields(StrEnum):
    NationalityFact = "Узнать национальность"
    ActivityFact = "Узнать вид деятельности"
    PhotoFact = "Узнать фото"
    FactsFact = "Узнать факт о человеке"
    AgeFactsFact = "Узнать факт про возраст"


class Persona:
    def __init__(self, name, birthdate, deathdate, nationality, activity, photo, facts):
        self.Name = name
        self.Nationality = nationality
        self.TypeOfActivity = activity
        self.NameOfPhotoFile = photo
        self.Facts = ["Факт: " + i for i in facts]
        birth_date = datetime.datetime.strptime(birthdate, DATETIME_MASK)
        death_date = datetime.datetime.strptime(deathdate, DATETIME_MASK)
        self.AgeFacts = ["Возраст: " + str(death_date.year - birth_date.year - (
                (death_date.month, death_date.day) < (birth_date.month, birth_date.day))),
                         "Дата рождения: " + birthdate,
                         "Дата смерти:" + deathdate]
        self.Left = {
            PersonFields.NationalityFact: 1,
            PersonFields.ActivityFact: 1,
            PersonFields.PhotoFact: 1,
            PersonFields.FactsFact: len(self.Facts),
            PersonFields.AgeFactsFact: len(self.AgeFacts)}

    def GetRandomFact(self):
        return random.choice(self.Facts)

    def GetRandomAgeFact(self):
        return random.choice(self.AgeFacts)
