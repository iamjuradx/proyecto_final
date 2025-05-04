from fastapi import APIRouter
from typing import List
from model.location import Location
from service.location_service import LocationService

router = APIRouter(prefix="/locations")
svc = LocationService(csv_path="divipola.csv")

@router.get("/", response_model=List[Location])
def all_locations():
    return svc.list_all()