from models import Persona
from services.json_service import GetRandomPerson


class Game:
    score: int
    CurrentPerson: Persona

    def __init__(self):
        self.CurrentPerson = await GetRandomPerson()
        self.score = 100

    def GuessName(self, name):
        # TODO norm check && const names
        if name == self.CurrentPerson.Name:
            return "Success"
        else:
            return "Wrong"

    def UseFact(self):
        pass
