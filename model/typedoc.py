from pydantic import BaseModel

class TypeDoc(BaseModel):
    code: str
    description: str