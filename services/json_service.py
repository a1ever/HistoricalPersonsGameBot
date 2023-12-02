import json
import random

from models.Persona import Persona

PathToJson = "../storage/gameData.json"


async def GetRandomPerson():
    with open(PathToJson, "rb") as personsFile:
        persons = json.load(personsFile)
        person = random.choice(persons)
        return Persona(
            person["name"],
            person["dateOfBirth"],
            person["dateOfDeath"],
            person["nationality"],
            person["typeOfActivity"],
            person["nameOfPhotoFile"],
            person["facts"])
