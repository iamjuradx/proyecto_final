from typing import List, Optional
from model.person import Person
from model.tree import Tree
from model.location import Location
from model.typedoc import TypeDoc

class PersonService:
    def __init__(self):
        # semilla de ejemplo (>18 años)
        example = [
            Person(id="1", first_name="Quijada",  last_name="Lopez", age=20, gender="M",
                   type_doc=TypeDoc(code="CC", description="Cédula Ciudadanía"),
                   location=Location(code="17001", name="Bogotá", department="Cundinamarca")),
            Person(id="2", first_name="Mateo",    last_name="Perez", age=25, gender="M",
                   type_doc=TypeDoc(code="TI", description="Tarjeta Identidad"),
                   location=Location(code="05001", name="Medellín", department="Antioquia")),
            Person(id="3", first_name="Jurado",   last_name="Gomez", age=30, gender="M",
                   type_doc=TypeDoc(code="CE", description="Cédula Extranjería"),
                   location=Location(code="18001", name="Pasto", department="Nariño")),
            Person(id="4", first_name="Aguilar",  last_name="Diaz", age=22, gender="F",
                   type_doc=TypeDoc(code="CC", description="Cédula Ciudadanía"),
                   location=Location(code="05001", name="Medellín", department="Antioquia")),
            Person(id="5", first_name="Marino",   last_name="Santos",age=28, gender="M",
                   type_doc=TypeDoc(code="TI", description="Tarjeta Identidad"),
                   location=Location(code="17001", name="Bogotá", department="Cundinamarca")),
        ]
        self.tree = Tree()
        for p in example:
            self.tree.add(p)

    def create(self, person: Person):
        if self.tree.find(person.id):
            raise ValueError("ID already exists")
        self.tree.add(person)

    def list_all(self) -> List[Person]:
        return self.tree.list_all()

    def get(self, person_id: str) -> Optional[Person]:
        return self.tree.find(person_id)

    def update(self, person: Person):
        if not self.tree.update(person):
            raise LookupError("Not found")

    def delete(self, person_id: str):
        if not self.tree.delete(person_id):
            raise LookupError("Not found")

    def list_by_location(self, code: str) -> List[Person]:
        return [p for p in self.tree.list_all() if p.location.code == code]

    def list_by_filter(self, doc_type: str, gender: str, loc_code: str) -> List[Person]:
        return [
            p for p in self.tree.list_all()
            if p.type_doc.code == doc_type and p.gender == gender and p.location.code == loc_code
        ]

    def list_with_adult_daughters(self) -> List[Person]:
        # padres que tengan al menos una hija mayor de edad
        result = []
        for p in self.tree.list_all():
            # buscar en children
            node = self.tree._find_node(self.tree.root, p.id)
            if node:
                for ch in node.children:
                    if ch.person.gender == "F" and ch.person.age >= 18:
                        result.append(p)
                        break
        return result