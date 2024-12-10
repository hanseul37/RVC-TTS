from pydantic import BaseModel

class Model(BaseModel):
    model_name: str
    wav: str
