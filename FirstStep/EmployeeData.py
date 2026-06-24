from pydantic import BaseModel
from typing import TypedDict

class EmployeeData(TypedDict):
    Name : str
    Contact :int
