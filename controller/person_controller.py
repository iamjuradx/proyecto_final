from fastapi import APIRouter, HTTPException
from typing import List
from model.person import Person
from service.person_service import PersonService

router = APIRouter(prefix="/persons")
svc = PersonService()

@router.get("/", response_model=List[Person])
def list_persons():
    return svc.list_all()

@router.post("/", response_model=None)
def create_person(person: Person):
    try:
        svc.create(person)
    except ValueError as e:
        raise HTTPException(400, str(e))

@router.get("/{person_id}", response_model=Person)
def get_person(person_id: str):
    p = svc.get(person_id)
    if not p:
        raise HTTPException(404, "Not found")
    return p

@router.put("/", response_model=None)
def update_person(person: Person):
    try:
        svc.update(person)
    except LookupError:
        raise HTTPException(404, "Not found")

@router.delete("/{person_id}", response_model=None)
def delete_person(person_id: str):
    try:
        svc.delete(person_id)
    except LookupError:
        raise HTTPException(404, "Not found")

@router.get("/by-location/{code}", response_model=List[Person])
def by_location(code: str):
    return svc.list_by_location(code)

@router.get("/by-filter", response_model=List[Person])
def by_filter(doc_type: str, gender: str, loc_code: str):
    return svc.list_by_filter(doc_type, gender, loc_code)

@router.get("/with-adult-daughters", response_model=List[Person])
def with_adult_daughters():
    return svc.list_with_adult_daughters()

@router.get("/parent/{person_id}", response_model=Person)
def get_parent(person_id: str):
    parent = svc.tree.find_parent(person_id)
    if not parent:
        raise HTTPException(404, "Not found")
    return parent