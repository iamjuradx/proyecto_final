import csv
from model.location import Location

class LocationService:
    def __init__(self, csv_path: str):
        try:
            self.list = self._load(csv_path)
        except FileNotFoundError:
            # Si no existe el CSV, inicializa con lista vacía
            self.list = []

    def _load(self, path: str) -> list[Location]:
        out: list[Location] = []
        with open(path, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for r in reader:
                out.append(Location(
                    code=r.get('MPIO_CODE', ''),
                    name=r.get('MPIO_NAME', ''),
                    department=r.get('DPTO_NAME', '')
                ))
        return out

    def list_all(self) -> list[Location]:
        return self.list

    def find(self, code: str) -> Location:
        for x in self.list:
            if x.code == code:
                return x
        return None