from pydantic import BaseModel

class TypeDoc(BaseModel):
    code: str
    description: str

    @classmethod
    def get_all(cls) -> list["TypeDoc"]:
        return [
            TypeDoc(code="CC", description="Cédula Ciudadanía"),
            TypeDoc(code="TI", description="Tarjeta Identidad"),
            TypeDoc(code="CE", description="Cédula Extranjería"),
        ]