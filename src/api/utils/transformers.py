import numpy as np
from category_encoders import BinaryEncoder
from src.api.config import ISSUE_STATUSES, DEFAULTS
from src.api.models.story_model import StoryModel

encoder = BinaryEncoder(cols=[0], return_df=True)
encoder.fit(np.array(ISSUE_STATUSES).reshape(-1, 1))

def transform_request_title(title: str) -> int:
    return len(set(title.split()))

def transform_request_description(description: str) -> dict:
    return {
        'Description_Unique_Words': len(set(description.split())),
        'Description_Length': len(description),
        'Description_Text_Unique_Words': len(set(description.strip("\"").split())),
        'Description_Text_Length': len(description.strip("\""))
    }

def transform_request_description_code(description_code: str) -> dict:
    return {
        'Description_Code_Unique_Words': len(set(description_code.split())),
        'Description_Code_Length': len(description_code)
    }

def encode_status(status: str) -> dict:
    encoded = encoder.transform(np.array([status]).reshape(-1, 1)).iloc[0].to_dict()
    encoded_statuses = {}
    for key, value in encoded.items():
        index = key.split("_")[-1]
        if index in {'0', '1', '2', '3', '6'}:
            new_key = f"Status_{index}"
            encoded_statuses[new_key] = value
    return encoded_statuses

def transform_request_data(data: StoryModel) -> dict:
    title_data = transform_request_title(data.title)
    desc_data = transform_request_description(data.description)
    desc_code_data = transform_request_description_code(data.description_code)
    status_data = encode_status(data.status)

    features_data = {
        'Jira_ID': DEFAULTS['Jira_ID'],
        'Total_Effort_Minutes': DEFAULTS['Total_Effort_Minutes'],
        'In_Progress_Minutes': DEFAULTS['In_Progress_Minutes'],
        'Resolution_Time_Minutes': DEFAULTS['Resolution_Time_Minutes'],
        'Story_Point_Changed_After_Estimation': DEFAULTS['Story_Point_Changed_After_Estimation'],
        'Sprint_ID': DEFAULTS['Sprint_ID'],
        'Resolution_1': DEFAULTS['Resolution_1'],
        'Resolution_0': DEFAULTS['Resolution_0'],
        'Title_Changed_After_Estimation': DEFAULTS['Title_Changed_After_Estimation'],
        'Resolution_3': DEFAULTS['Resolution_3'],
        'Assignee_ID': DEFAULTS['Assignee_ID'],
        'Resolution_5': DEFAULTS['Resolution_5'],
        'Title_Unique_Words': title_data,
        'Title_Length': len(data.title),
        **desc_data,
        **desc_code_data,
        **status_data
    }
    return features_data
