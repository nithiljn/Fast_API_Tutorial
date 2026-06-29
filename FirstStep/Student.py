from pydantic import BaseModel, Field

class Student(BaseModel):
    Name : str = Field(
        ...,description= "Student Name"
    )
    Branch:str = Field(
          ..., description="Student branch"
    )
    Year :int = Field(
        description="Current Year of the Student"
    )

    # age : int = Field(
    #     description="Student Age"
    # )

