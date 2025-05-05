from pydantic import BaseModel

class BookIn(BaseModel):
    title: str
    author: str
    year: int

class BookOut(BookIn):
    id: int


class clientIn(BaseModel):
    source:str
    destination:str
    noOfDdays:int
    TravelPreference:str
    AccPreference:str
    FoodSuggestion:bool
    Sightseeing:int

