from pydantic import BaseModel, conint, field_validator
from src.api.config import ISSUE_STATUSES

class StoryModel(BaseModel):
    title: str
    description: str = 'No description'
    description_code: str = 'No description code'
    status: str = 'To Do'

    @field_validator('status')
    @classmethod
    def validate_story_status(cls, status: str) -> str:
        allowed_status = ', '.join(ISSUE_STATUSES)
        if status not in ISSUE_STATUSES:
            raise ValueError(f'Invalid story_status. Allowed values are [{allowed_status}]')
        return status
