from pydantic import BaseModel, conint, confloat#, field_validator

class StoryModel(BaseModel):
    # title: str
    # description: str
    # status: str
    # priority: str
    # ID: int
    # Jira_ID: int
    # Status_0: conint(ge=0, le=1)
    # Status_1: conint(ge=0, le=1)
    # Status_2: conint(ge=0, le=1)
    # Status_3: conint(ge=0, le=1)
    # Status_4: conint(ge=0, le=1)
    # Status_5: conint(ge=0, le=1)
    # Status_6: conint(ge=0, le=1)
    # Resolution_0: conint(ge=0, le=1)
    # Resolution_1: conint(ge=0, le=1)
    # Resolution_2: conint(ge=0, le=1)
    # Resolution_3: conint(ge=0, le=1)
    # Resolution_4: conint(ge=0, le=1)
    # Resolution_5: conint(ge=0, le=1)
    # Story_Point: confloat(ge=0)
    # In_Progress_Minutes: confloat(ge=0)
    # Total_Effort_Minutes: confloat(ge=0)
    # Resolution_Time_Minutes: confloat(ge=0)
    # Title_Changed_After_Estimation: conint(ge=0, le=1)
    # Description_Changed_After_Estimation: conint(ge=0, le=1)
    # Story_Point_Changed_After_Estimation: conint(ge=0, le=1)
    # Creator_ID: float
    # Reporter_ID: float
    # Assignee_ID: float
    # Project_ID: int
    # Sprint_ID: float
    # Has_Resolution_Date: conint(ge=0, le=1)
    # Time_To_Estimate_Minutes: int
    # Title_Length: float
    # Title_Unique_Words: float
    # Description_Length: float
    # Description_Unique_Words: float
    # Description_Text_Length: float
    # Description_Text_Unique_Words: float
    # Description_Code_Length: float
    # Description_Code_Unique_Words: float
    Story_Point_Changed_After_Estimation: float
    In_Progress_Minutes: float
    Sprint_ID: float
    Status_4: int
    Time_To_Estimate_Minutes: int
    Title_Changed_After_Estimation: int
    Total_Effort_Minutes: float
    Project_ID: int
    Resolution_5: int
    ID: int

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