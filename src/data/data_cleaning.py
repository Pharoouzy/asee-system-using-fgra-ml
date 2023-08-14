import numpy as np
import pandas as pd


class DataCleaning:

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Execute all data cleaning operations."""
        # Assess missing data
        self.assess_missing_data(df)

        # TODO: Implement imputation strategies based on the assessment

        # Remove duplicates
        df = self.remove_duplicates(df)

        # Handle outliers for specific columns
        columns_with_outliers = ['Timespent', 'In_Progress_Minutes', 'Total_Effort_Minutes']
        df = self.remove_outliers(df, columns_with_outliers)

        # Handle negative time durations
        time_columns = ['Timespent', 'In_Progress_Minutes', 'Total_Effort_Minutes', 'Resolution_Time_Minutes']
        df = self.handle_negative_times(df, time_columns)

        return df

    @staticmethod
    def assess_missing_data(df: pd.DataFrame) -> pd.DataFrame:
        """Assess missing data."""
        missing_data = df.isnull().sum()
        missing_data = missing_data[missing_data > 0]
        missing_data = missing_data.sort_values(ascending=False)
        missing_data = missing_data.reset_index()
        missing_data = missing_data.rename(columns={'index': 'Column', 0: 'Missing_Data_Count'})
        missing_data = missing_data[missing_data['Missing_Data_Count'] > 0]
        missing_data = missing_data.sort_values(by='Missing_Data_Count', ascending=False)
        missing_data = missing_data.reset_index(drop=True)
        return missing_data

    @staticmethod
    def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
        """Remove duplicates."""
        df = df.drop_duplicates()
        return df

    @staticmethod
    def remove_outliers(df: pd.DataFrame, columns_with_outliers: list) -> pd.DataFrame:
        """Remove outliers."""
        for column in columns_with_outliers:
            df[column] = np.where(df[column] < 0, 0, df[column])
        return df

    @staticmethod
    def handle_negative_times(df: pd.DataFrame, time_columns: list) -> pd.DataFrame:
        """Handle negative time durations."""
        for column in time_columns:
            df[column] = np.where(df[column] < 0, 0, df[column])
        return df

    @staticmethod
    def assess_missing_datax(df: pd.DataFrame) -> None:
        """Print out missing data statistics for the dataframe."""
        missing_data = df.isnull().sum()
        percent_missing = (df.isnull().sum() / df.isnull().count() * 100)
        missing_data_table = pd.concat([missing_data, percent_missing], axis=1,
                                       keys=['Total Missing', 'Percent Missing (%)'])
        print(missing_data_table[missing_data_table['Total Missing'] > 0].sort_values('Percent Missing (%)', ascending=False))