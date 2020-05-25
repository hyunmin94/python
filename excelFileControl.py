import pandas as pd

df = pd.read_excel('C:/myPyCode/data/학생시험성적.xlsx', sheet_name = '2차시험', index_col='학생')
print(df)


