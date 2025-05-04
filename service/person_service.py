from model.person import Person
from model.tree import Tree

class PersonService:
    def __init__(self):
        self.tree = Tree()

    def create(self, p: Person):
        if self.tree.find(p.id):
            raise ValueError("exists")
        self.tree.add(p)

    def list_all(self) -> list[Person]:
        return self.tree.list_all()

    def get(self, id: str) -> Person:
        x = self.tree.find(id)
        if not x:
            raise ValueError("not found")
        return x

    def update(self, p: Person):
        if not self.tree.update(p):
            raise ValueError("not found")

    def delete(self, id: str):
        if not self.tree.delete(id):
            raise ValueError("not found")

    def by_location(self, code: str) -> list[Person]:
        return [p for p in self.list_all() if p.location.code == code]

    def by_doc_gender_loc(self, doc: str, gender: str, loc: str) -> list[Person]:
        return [
            p for p in self.list_all()
            if p.type_doc.code==doc and p.gender==gender and p.location.code==loc
        ]

    def adult_daughters(self) -> list[Person]:
        c = self.tree.root.children if self.tree.root else []
        return [n.person for n in c if n.person.age>=18]