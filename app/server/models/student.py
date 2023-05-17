from typing import Optional

from fastapi.responses import JSONResponse
from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Dunny",
                "email": "jdunny@x.edu.us",
                "course_of_study": "Mechanical resources engineering",
                "year": 2,
                "gpa": "3.0",
            }
        }


class UpdateStudentModel(BaseModel):
    fullname: Optional[str]
    email: Optional[str]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "John Dunny",
                "email": "jdunny@x.edu.us",
                "course_of_study": "Mechanical resources and civil engineering",
                "year": 4,
                "gpa": "4.0",
            }
        }


def ResponseModel(data: dict, code: int, message: str):
    response = {
        "data": [data],
        "code": code,
        "message": message,
    }
    return JSONResponse(content=response, status_code=response.get("code"))


def ErrorResponseModel(error, code, message):
    response = {
        "error": error,
        "code": code,
        "message": message,
    }
    return JSONResponse(content=response, status_code=response.get("code"))
