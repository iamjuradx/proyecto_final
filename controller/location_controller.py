from fastapi import APIRouter, HTTPException
from typing import List
from model.location import Location
from service.location_service import LocationService

router = APIRouter(prefix="/locations")
svc = LocationService()

@router.get("/", response_model=List[Location])
def all_locations():
    return svc.get_all()

@router.get("/{code}", response_model=Location)
def get_location(code: str):
    loc = svc.get_by_code(code)
    if not loc:
        raise HTTPException(404, "Not found")
    return loc

@router.get("/department/{dept}", response_model=List[Location])
def by_department(dept: str):
    return svc.get_by_department(dept)