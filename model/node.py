from typing import List, Optional
from .person import Person

class Node:
    def __init__(self, person: Person):
        self.person = person
        self.children: List[Node] = []
        self.parent: Optional[Node] = None

    def add_child(self, child: "Node"):
        child.parent = self
        self.children.append(child)

    def remove_child(self, person_id: str):
        # elimina el hijo cuyo person.id coincide
        self.children = [c for c in self.children if c.person.id != person_id]
