from dataclasses import dataclass
import string


@dataclass
class Person:
    def __init__(self, name, surname, discord_id):
        self.name: string = ""
        self.surname: string = ""
        self.discord_id: int = 0
