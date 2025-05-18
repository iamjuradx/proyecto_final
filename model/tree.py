from typing import Optional, List
from .node import Node
from .person import Person

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
        # simple: comparar por id
        if new_node.person.id < current.person.id:
            # hijo izquierdo
            if current.children:
                self._add(current.children[0], new_node)
            else:
                current.add_child(new_node)
        else:
            # hijo derecho
            if len(current.children) > 1:
                self._add(current.children[1], new_node)
            else:
                current.add_child(new_node)

    def find(self, person_id: str) -> Optional[Person]:
        return self._find(self.root, person_id)

    def _find(self, node: Optional[Node], person_id: str) -> Optional[Person]:
        if node is None:
            return None
        if node.person.id == person_id:
            return node.person
        # buscar recursivamente
        for child in node.children:
            found = self._find(child, person_id)
            if found:
                return found
        return None

    def list_all(self) -> List[Person]:
        result: List[Person] = []
        def collect(n: Optional[Node]):
            if n:
                result.append(n.person)
                for ch in n.children:
                    collect(ch)
        collect(self.root)
        return result

    def update(self, person: Person) -> bool:
        # retorna True si lo encontró y actualizó
        return self._update(self.root, person)

    def _update(self, node: Optional[Node], person: Person) -> bool:
        if node is None:
            return False
        if node.person.id == person.id:
            node.person = person
            return True
        for ch in node.children:
            if self._update(ch, person):
                return True
        return False

    def delete(self, person_id: str) -> bool:
        # si es root
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
        for ch in node.children:
            if self._delete(ch, person_id):
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
        for ch in node.children:
            found = self._find_node(ch, person_id)
            if found:
                return found
        return None