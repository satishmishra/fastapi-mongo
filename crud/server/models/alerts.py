from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class AlertSchema(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    email: EmailStr = Field(...)
    status: str = Field(...)
    severity: str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "name": "Phishing Email",
                "description": "phising email ",
                "email": "jdoe@x.edu.ng",
                "status": "open",
                "severity": "unknown",
            }
        }


class UpdateAlertModel(BaseModel):
    name: Optional[str]
    description: Optional[str]
    email: Optional[EmailStr]
    status: Optional[str]
    severity: Optional[int]

    class Config:
        schema_extra = {
            "example": {
                "name": "Phishing Email",
                "email": "jdoe@x.edu.ng",
                "status": "open",
                "severity": "unknown",
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
