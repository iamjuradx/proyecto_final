from pydantic import BaseModel
from model.location import Location
from model.typedoc import TypeDoc

class Person(BaseModel):
    id: str
    first_name: str
    last_name: str
    age: int
    gender: str
    type_doc: TypeDoc
    location: Location