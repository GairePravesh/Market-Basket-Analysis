import pandas as pd

# df = pd.read_csv("overall.csv")
# to_drop = ["Class", "Gender", "Student's Name", "Type", "School Type", "School Name", "District"]
# df.drop(columns=to_drop, inplace=True)
# n_df = df.loc[(df!=0).all(axis=1)]
# n_df.to_csv("cleaned.csv", encoding="utf-8", index=False)

# def marksToGrades(mark):
#     if mark > 79: 
#         return "A"
#     elif mark > 59: 
#         return "B"
#     elif mark > 31: 
#         return "C"
#     else: 
#         return "D"

# df = pd.read_csv("cleaned.csv")
# n_df = df.applymap(marksToGrades)
# n_df.to_csv("grades.csv", encoding="utf-8", index=False)

# df = pd.read_csv("grades.csv")
# col_names =  [x for x in df]
# n_df = pd.DataFrame(columns = col_names)
# for name in col_names:
#     n_df[name] = df[name].apply(lambda x: name[:2].lower() + x)
# n_df.to_csv("data.csv", encoding="utf-8", index=False)

# df = pd.read_csv("data.csv")
# print(df['Maths'].value_counts())
