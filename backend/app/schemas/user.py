from pydantic import BaseModel, Field

class UserSchema(BaseModel):
    name: str
    age: int = Field(ge=0, le=130)