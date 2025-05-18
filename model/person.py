from pydantic import BaseModel
from .location import Location
from .typedoc import TypeDoc

class Person(BaseModel):
    id: str
    first_name: str
    last_name: str
    age: int
    gender: str
    type_doc: TypeDoc
    location: Location
