from typing import List
from model.person import Person

class Node:
    def __init__(self, person: Person):
        self.person = person
        self.children: List[Node] = []

    def add_child(self, child: "Node"):
        self.children.append(child)

    def remove_child(self, person_id: str):
        self.children = [c for c in self.children if c.person.id != person_id]