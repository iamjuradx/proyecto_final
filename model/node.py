from typing import List, Optional
from model.person import Person

class Node:
    def __init__(self, person: Person):
        self.person = person
        self.children: List["Node"] = []
        self.parent: Optional["Node"] = None  # 🔸 Nuevo atributo (V2)

    def add_child(self, child: "Node"):
        child.parent = self               # 🔸 Establecer el padre
        self.children.append(child)

    def remove_child(self, person_id: str):
        for i, child in enumerate(self.children):
            if child.person.id == person_id:
                child.parent = None       # 🔸 Limpiar referencia al padre
                del self.children[i]
                break