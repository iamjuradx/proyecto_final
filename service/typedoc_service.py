from model.typedoc import TypeDoc

class TypeDocService:
    def get_all(self) -> list[TypeDoc]:
        return TypeDoc.get_all()