import pandas as pd

def extract_text_based_features(data: pd.DataFrame, columns: List[str]) -> pd.DataFrame:
    # Extract text-based features for 'Title', 'Description', 'Description_Text', 'Description_Code' columns
    new_columns = []

    for column in columns:
        # Length of the text
        length_column = f'{column}_Length'
        data[length_column] = data[column].apply(len)
        new_columns.append(length_column)
        # Number of unique words
        unique_words_column = f'{column}_Unique_Words'
        data[unique_words_column] = data[column].apply(lambda x: len(set(x.split())))
        new_columns.append(unique_words_column)

    # Check the first few rows to verify the new columns
    data[new_columns].head()

    return data