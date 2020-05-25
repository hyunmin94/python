import pandas as pd

excel_exam_data1 = {'학생': ['A','B','C','D','E','F'],
                    '국어': [80,90,40,50,20,50],
                    '영어': [85,95,90,60,70,80],
                    '수학': [40,60,70,80,90,100]}

excel_exam_data2 = {'학생': ['A','B','C','D','E','F'],
                    '국어': [86,90,45,50,80,50],
                    '영어': [86,95,95,65,70,85],
                    '수학': [45,60,75,80,95,100]}

df1 = pd.DataFrame(excel_exam_data1, columns =['학생','국어','영어','수학'])
df2 = pd.DataFrame(excel_exam_data2, columns =['학생','국어','영어','수학'])
excel_writer = pd.ExcelWriter('C:/myPyCode/data/학생시험성적종합.xlsx', engine='xlsxwriter')
df1.to_excel(excel_writer, index=False, sheet_name='중간고사')
df2.to_excel(excel_writer, index=False, sheet_name='기말고사')
excel_writer.save()


