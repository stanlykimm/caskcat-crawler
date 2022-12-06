from datetime import datetime
from typing import Optional

from bson import ObjectId
from pydantic import BaseModel
from pydantic import Field

from models.mongodb import PyObjectId


class BaseCollectionModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias='_id')

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class Brand(BaseModel):
    id: str
    kr: str
    eng: str
