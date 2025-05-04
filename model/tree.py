from typing import Optional, List
from model.node import Node
from model.person import Person

class Tree:
    def __init__(self):
        self.root: Optional[Node] = None

    def add(self, person: Person):
        node = Node(person)
        if self.root is None:
            self.root = node
        else:
            self._add(self.root, node)

    def _add(self, current: Node, new_node: Node):
        # very simple: compare by id string
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
        return self._find(self.root, person_id)

    def _find(self, node: Optional[Node], person_id: str):
        if node is None:
            return None
        if node.person.id == person_id:
            return node.person
        for c in node.children:
            res = self._find(c, person_id)
            if res:
                return res
        return None

    def list_all(self) -> List[Person]:
        out: List[Person] = []
        def dfs(n: Optional[Node]):
            if n:
                out.append(n.person)
                for c in n.children:
                    dfs(c)
        dfs(self.root)
        return out

    def update(self, person: Person) -> bool:
        return self._update(self.root, person)

    def _update(self, node: Optional[Node], person: Person) -> bool:
        if node is None:
            return False
        if node.person.id == person.id:
            node.person = person
            return True
        for c in node.children:
            if self._update(c, person):
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
        for c in node.children:
            if self._delete(c, person_id):
                return True
        return False