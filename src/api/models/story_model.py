from pydantic import BaseModel#, field_validator

class StoryModel(BaseModel):
    story_type: str
    story_status: str
    complexity: str
    work_days: float
    resources: float
    # ... Add all the other feature names and types

    # TODO: Add validation for story model
    # @field_validator('story_type')
    # def validate_story_type(self, story_type) -> str:
    #     valid_types = ['bug', 'enhancement', 'task']
    #     if story_type not in valid_types:
    #         raise ValueError(f'Invalid story_type. Allowed values are {valid_types}')
    #     return story_type
    #
    # @field_validator('story_status')
    # def validate_story_status(self, story_status):
    #     valid_types = ['To Do', 'Complete', 'In Progress', 'Done']
    #     if story_status not in valid_types:
    #         raise ValueError(f'Invalid story_status. Allowed values are {story_status}')
    #     return story_status