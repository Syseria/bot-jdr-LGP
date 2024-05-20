from dataclasses import dataclass
from Person_Class import Person
import string


@dataclass
class Table:
    def __init__(self):
        self.DM: string = ""
        self.one_shot_name: string = ""
        self.start_hours: int = 0
        self.start_minutes: int = 0
        self.duration_hours: int = 0
        self.duration_minutes: int = 0
        self.duration: int = 0
        self.MAX_NUMBER_OF_PLAYERS: int = 0
        self.participants = []
        self.players = []
        self.wait_list = []

    def add_participant(self, name, surname, discord_id):
        if Person(name, surname, discord_id) in self.participants:
            print(f"{discord_id} déjà inscrit à {self.one_shot_name}.")
            return

        if Person(name, surname, discord_id) in self.players:
            print(f"{discord_id} déjà inscrit à {self.one_shot_name} comme joueur !")
            return

        if Person(name, surname, discord_id) in self.wait_list:
            print(f"{discord_id} déjà inscrit à {self.one_shot_name} comme réserve !")
            return

        if len(self.players) < self.MAX_NUMBER_OF_PLAYERS:
            self.players.append(Person(name, surname, id))
            print(f"{id} ajouté à {self.one_shot_name} comme joueur !")
        else:
            self.wait_list.append(Person(name, surname, id))
            print(f"{id} ajouté à {self.one_shot_name} comme réserve !")

        self.participants.append(Person(name, surname, discord_id))
