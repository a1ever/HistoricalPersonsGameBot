import random


class Persona:
    def __init__(self, name, birthdate, death_date, nationality, activity, photo, facts):
        self.Name = name
        self.DateOfBirth = birthdate
        self.DateOfDeath = death_date
        self.Nationality = nationality
        self.TypeOfActivity = activity
        self.NameOfPhotoFile = photo
        self.Facts = facts

    def GetRandomFact(self):
        return random.choice(self.Facts)