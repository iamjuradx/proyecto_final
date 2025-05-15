from typing import Optional, List
from model.node import Node
from model.person import Person

class Tree:
    def __init__(self):
        self.root: Optional[Node] = None

    def add(self, person: Person):
        new_node = Node(person)
        if self.root is None:
            self.root = new_node
        else:
            self._add(self.root, new_node)

    def _add(self, current: Node, new_node: Node):
        # Simple comparison using the person's ID
        if new_node.person.id < current.person.id:
            if current.children:
                self._add(current.children[0], new_node)
            else:
                current.add_child(new_node)
        else:
            if len(current.children) > 1:
                self._add(current.children[1], new_node)
            else:
                current.add_child(new_node)

    def find(self, person_id: str) -> Optional[Person]:
        return self._find_person(self.root, person_id)

    def _find_person(self, node: Optional[Node], person_id: str):
        if node is None:
            return None
        if node.person.id == person_id:
            return node.person
        for child in node.children:
            result = self._find_person(child, person_id)
            if result:
                return result
        return None

    def list_all(self) -> List[Person]:
        people: List[Person] = []

        def walk(node: Optional[Node]):
            if node:
                people.append(node.person)
                for child in node.children:
                    walk(child)

        walk(self.root)
        return people

    def update(self, person: Person) -> bool:
        return self._update(self.root, person)

    def _update(self, node: Optional[Node], person: Person) -> bool:
        if node is None:
            return False
        if node.person.id == person.id:
            node.person = person
            return True
        for child in node.children:
            if self._update(child, person):
                return True
        return False

    def delete(self, person_id: str) -> bool:
        if self.root and self.root.person.id == person_id:
            self.root = None
            return True
        return self._delete(self.root, person_id)

    def _delete(self, node: Optional[Node], person_id: str) -> bool:
        if node is None:
            return False
        before = len(node.children)
        node.remove_child(person_id)
        if len(node.children) < before:
            return True
        for child in node.children:
            if self._delete(child, person_id):
                return True
        return False

    def find_parent(self, person_id: str) -> Optional[Person]:
        node = self._find_node(self.root, person_id)
        if node and node.parent:
            return node.parent.person
        return None

    def _find_node(self, node: Optional[Node], person_id: str) -> Optional[Node]:
        if node is None:
            return None
        if node.person.id == person_id:
            return node
        for child in node.children:
            result = self._find_node(child, person_id)
            if result:
                return result
        return None