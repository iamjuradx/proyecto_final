import os
from typing import List
from model.location import Location

class LocationService:
    def __init__(self):
        # determina ruta absoluta donde está este archivo
        base = os.path.dirname(__file__)           # .../FastAPIDivipola/service
        root = os.path.dirname(base)               # .../FastAPIDivipola
        csv_path = os.path.join(root, "divipola.csv")
        print(">>> Loading CSV from:", csv_path)
        self.list: List[Location] = Location.load_all(csv_path)

    def get_all(self) -> List[Location]:
        return self.list

    def get_by_code(self, code: str) -> Location | None:
        for loc in self.list:
            if loc.code == code:
                return loc
        return None

    def get_by_department(self, dept: str) -> List[Location]:
        return [loc for loc in self.list if loc.department == dept]