import pandas as pd

class StudentCategorizer:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.categories = {
            'The_Pirates': (14, 18),
            'The_Yankees': (18, 22),
            'The_Bulls': (22, 25)
        }
        self.categorized_students = {category: pd.DataFrame() for category in self.categories}

    def read_csv(self):
        return pd.read_csv(self.csv_file)

    def categorize(self, df):
        temp_dfs = {category: [] for category in self.categories}
        
        for index, row in df.iterrows():
            age = row['Age']
            for category, (age_min, age_max) in self.categories.items():
                if age_min < age <= age_max:
                    temp_dfs[category].append(row)
                    break
            else:
                if age > 25:
                    self.handle_error(age)
        
        for category, rows in temp_dfs.items():
            if rows:
                self.categorized_students[category] = pd.DataFrame(rows)

    def handle_error(self, age):
        print(f"Error: Age {age} is out of the categorization range.")

    def save_and_display_categories(self):
        for category, data in self.categorized_students.items():
            if not data.empty:
                filename = f"{category}.csv"
                data.to_csv(filename, index=False)
                print(f"{category} group saved to {filename}")
                print(data)

# Usage
csv_file = "C:/Users/ipinu/OneDrive/Documents/S.YusufCOS102/week-11/SIS.csv"
categorizer = StudentCategorizer(csv_file)
df = categorizer.read_csv()
categorizer.categorize(df)
categorizer.save_and_display_categories()
