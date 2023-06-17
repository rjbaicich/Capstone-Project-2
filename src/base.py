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
        # Reads the CSV file and loads the data into a pandas DataFrame.
        self.df = pd.read_csv(self.csv_file)
        return self.df

    def clean_data(self):
        # Cleans the data by removing duplicates and handling missing values.
        # Remove duplicates
        self.df.drop_duplicates(inplace=True)

        # Handle missing values
        self.df.fillna(0, inplace=True)

        # Changing Data Types
        self.df.convert_dtypes()

    def add_endangered_score(self):
        # Adds an 'Endangered Score' column based on the 'SUMCOUNT' values.
        self.df['Endangered Score'] = self.df['SUMCOUNT'].apply(lambda x: '1 Extreme' if 0 <= x <= 100
                                                               else '2 High' if 101 <= x <= 500
                                                               else '3 Medium' if 501 <= x <= 1000
                                                               else '4 Low')

if __name__ == '__main__':
    csv_file = r'C:\Users\RedneckRandy\Documents\GitHub\Capstone-Project-2\Combined_Less.csv'
    c = Base(csv_file)
    print(c.return_string())
    print(c.df)
    c.df.to_csv('endangered_clean.csv')

