from fastapi import APIRouter, HTTPException
from typing import List
from model.person import Person
from service.person_service import PersonService

router = APIRouter(prefix="/persons")
svc = PersonService()

@router.post("/", response_model=dict)
def create(p: Person):
    try:
        svc.create(p)
        return {"msg":"created"}
    except ValueError:
        raise HTTPException(400,"exists")

@router.get("/", response_model=List[Person])
def list_all():
    return svc.list_all()

@router.get("/{id}", response_model=Person)
def get_one(id: str):
    try:
        return svc.get(id)
    except ValueError:
        raise HTTPException(404,"not found")

@router.put("/", response_model=dict)
def update(p: Person):
    try:
        svc.update(p)
        return {"msg":"updated"}
    except ValueError:
        raise HTTPException(404,"not found")

@router.delete("/{id}", response_model=dict)
def delete(id: str):
    try:
        svc.delete(id)
        return {"msg":"deleted"}
    except ValueError:
        raise HTTPException(404,"not found")

@router.get("/by-location/{code}", response_model=List[Person])
def by_loc(code: str):
    return svc.by_location(code)

@router.get("/by-filter", response_model=List[Person])
def by_filter(doc: str, gender: str, loc: str):
    return svc.by_doc_gender_loc(doc, gender, loc)

@router.get("/adult-daughters", response_model=List[Person])
def adults():
    return svc.adult_daughters()