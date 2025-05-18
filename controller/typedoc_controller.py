from fastapi import APIRouter
from typing import List
from model.typedoc import TypeDoc
from service.typedoc_service import TypeDocService

router = APIRouter(prefix="/typedocs")
svc = TypeDocService()

@router.get("/", response_model=List[TypeDoc])
def all_types():
    return svc.get_all()