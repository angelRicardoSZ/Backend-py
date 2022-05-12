from doctest import Example
from email.policy import default
from typing import Optional
from enum import Enum

from pydantic import BaseModel
from pydantic import Field

from fastapi import FastAPI
from fastapi import Body, Query, Path
app = FastAPI()

# Models
class HairColor(Enum):
    white = "white"
    brown = "brown"
    black = "black"
    blonde = "blonde"
    red = "red"
    


class Location(BaseModel):
    city: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Puebla"
        )
    state: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="Puebla"
        )
    country: str = Field(
        ...,
        min_length=1,
        max_length=50,
        example="México"
        )


class Person(BaseModel):
    first_name: str = Field(
        ...,
        min_length=1,
        max_length=50, 
        example= "Ricardo"
        )
    last_name: str =  Field(
        ...,
        min_length=1,
        max_length=50,
        example="Zefe"
        )
    age: int = Field(
        ...,
        gt=0,
        le=115,
        example=25
    )
    hair_color: Optional[HairColor] = Field(default=None,example="black")
    is_married: Optional[bool] = Field(default = None,example=False)
    
    # class Config:
    #     schema_extra = {
    #         "Facundo": {
    #             "First_name": "Angel",
    #             "last_name":"Sanchez",
    #             "age":21,
    #             "hair_color": "blonde",
    #             "Is married": False
    #         }
    #     }
    
@app.get("/")
def home():
    return {"Hello":"World"}

# Request and response body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person
    
    
# Validaciones: Query Parameters
@app.get("/person/detail")
def show_person(
    name: Optional[str] = Query(
        None,
        min_length=1, 
        max_length=50,
        title="Person Name",
        description="This is the person name. It's between 1 and 50 characters",
        example="Pedro"
        ),
    age: str = Query(
        ...,
        title="Person Age",
        description="This is the person age. It's required",
        example=20
        )
): 
    return {name: age}

# Validaciones: Path Parameters
@app.get("/person/detail/{person_id}")
def show_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="Person ID",
        description="This is the person ID. It's reqiuired and it's more than 0.",
        example=123
        )
): 
    return {person_id: "It exists!"}

# Validaciones: Request Body

@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        title="PERSON_ID",
        desciption="This is the person ID",
        gt=0,
        example=40        
    ),
    person: Person = Body(...),
    location: Location = Body(...)
):
    results = person.dict()
    results.update(location.dict())
    return results