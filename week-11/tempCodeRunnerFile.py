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