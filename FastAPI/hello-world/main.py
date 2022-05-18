from distutils.command.upload import upload
from doctest import Example
from email import message
from email.header import Header
from email.policy import default
from optparse import Option
from typing import Optional
from enum import Enum
from urllib import response

from pydantic import BaseModel
from pydantic import Field
from pydantic import EmailStr

from fastapi import FastAPI
from fastapi import status
from fastapi import Body, Query, Path, Form, Header, Cookie, UploadFile, File
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

class PersonBase(BaseModel):
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
class Person(PersonBase):
    passwrod: str = Field(...,min_length=8)
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
class PersonOut(PersonBase):
    pass
    
class LoginOut(BaseModel):
    username: str = Field(
        ...,
        max_Length=20,
        example="miguel2022",
        )
    message: str = Field(
        default="Login Succesfully!"
    )

    
@app.get(
    path="/",
    status_code=status.HTTP_200_OK
    )
def home():
    return {"Hello":"World"}

# Request and response body
@app.post(
    path="/person/new",
    response_model=PersonOut,
    status_code=status.HTTP_201_CREATED    
    )
def create_person(person: Person = Body(...)):
    return person
    
    
# Validaciones: Query Parameters
@app.get(
    path="/person/detail",
    status_code=status.HTTP_200_OK
    )
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
@app.get(
    path="/person/detail/{person_id}",
    status_code=status.HTTP_200_OK
    )
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

@app.put(
    path="/person/{person_id}",
    status_code=status.HTTP_201_CREATED
    )
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

# Forms
@app.post(
    path="/login",
    response_model=LoginOut,
    status_code=status.HTTP_200_OK
)
def login(
    username: str = Form(...),
    password: str=Form(...)
    ):
    return LoginOut(username=username)


# Cookies and headers parameters
@app.post(
    path="/contact",
    status_code=status.HTTP_200_OK
)
def contact(
    first_name: str=Form(
        ...,
        max_length=20,
        min_length=1
    ),
    last_name: str=Form(
        ...,
        max_length=20,
        min_length=1
    ),
    email: EmailStr = Form(
        ...
    ),
    message: str=Form(
        ...,
        min_length=20
    ),
    user_agent: Optional[str] = Header(default=None),
    ads:Optional[str]=Cookie(default=None)
    
):
    return user_agent

# Files
@app.post(
    path="/post-image"
)
def post_image(
    image: UploadFile = File(...)
):
    return {
        "Filename": image.filename,
        "Format": image.content_type,
        "Size(kb)": round(len(image.file.read())/1024, ndigits=2)
    }