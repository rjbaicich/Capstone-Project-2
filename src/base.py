import pandas as pd

class Base:
    def __init__(self, csv_file):
        self.df = None
        self.csv_file = csv_file
        self.get_data()
        self.clean_data()
        self.add_endangered_score()

    def return_string(self):
        return self.csv_file

    def get_data(self):
        #Reads the CSV file and loads the data into a pandas DataFrame.
        self.df = pd.read_csv(self.csv_file, dtype={'sumcount': 'Int64'}, low_memory=False)
        return self.df

    def clean_data(self):
        #Remove duplicates
        self.df.drop_duplicates(inplace=True)

        #Handle missing values
        self.df.fillna(0, inplace=True)

        #Changing Data Types
        self.df = self.df.convert_dtypes()

    def add_endangered_score(self):
        #Adds an 'Endangered Score' column based on the 'SUMCOUNT' values.
        self.df['Endangered Score'] = self.df['sumcount'].apply(lambda x: '1 Extreme' if 0 <= x <= 100
                                                               else '2 High' if 101 <= x <= 500
                                                               else '3 Medium' if 501 <= x <= 1000
                                                               else '4 Low')

    def get_data_by_common_name(self, common_name):
        #Retrieves fish data based on the selected common name.
        fish_data = self.df[self.df['common_name'] == common_name]
        if not fish_data.empty:
            return fish_data.iloc[0]
        else:
            return pd.Series(dtype='object')