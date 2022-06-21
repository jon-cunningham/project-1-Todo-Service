from pydantic import BaseModel

class TodoOut(BaseModel):
    id: str
    title: str
    notes: str
    status: str

    class Config:
        schema_extra = {
            "example": {
                "id": "uuid",
                "title": "Task_to_complete",
                "notes": "Add_a_note",
                "status": "Task in progress",
            }
        }

class TodoIn(BaseModel):
    title: str
    notes: str
    status: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Task_to_complete",
                "notes": "Add_a_note",
                "status": "Task in progress",
            }
        }

class TodoReadAll(BaseModel):
    id: str
    title: str
    notes: str
    status: str

    class Config:
        schema_extra = {
            "example": {
                "title": "Task_to_complete",
                "notes": "Add_a_note",
                "status": "Task in progress",
            }
        }