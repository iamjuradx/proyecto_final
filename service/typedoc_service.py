from model.typedoc import TypeDoc

class TypeDocService:
    def __init__(self):
        self.list = [
            TypeDoc(code='CC', description='Cédula'),
            TypeDoc(code='TI', description='Tarjeta identidad'),
            TypeDoc(code='PP', description='Pasaporte'),
        ]

    def list_all(self) -> list[TypeDoc]:
        return self.list

    def find(self, code: str) -> TypeDoc:
        for x in self.list:
            if x.code == code:
                return x
        return None