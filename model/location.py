from pydantic import BaseModel

class Location(BaseModel):
    code: str
    name: str
    department: str

    @classmethod
    def load_all(cls, path: str) -> list["Location"]:
        """Lee el CSV línea a línea y crea Location."""
        items = []
        text = open(path, encoding="utf-8").read().splitlines()
        for line in text[1:]:  # saltar cabecera
            cols = line.split(",")
            # DIVIPOLA tiene columnas: municipality_code,municipality_name,department_name,...
            loc = Location(
                code=cols[0],
                name=cols[1],
                department=cols[2]
            )
            items.append(loc)
        return items