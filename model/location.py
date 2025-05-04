from pydantic import BaseModel

class Location(BaseModel):
    code: str
    name: str
    department: str