import pandas as pd

data_series1=pd.Series([10,20,30,40])
print(data_series1)

data_series2=pd.Series([12,13,14,15,16],['a','b','c','d','e'])
print(data_series2)

print(data_series1[1])
print(data_series2['b'])
print(data_series1.mean())
print(data_series1[data_series1>14])

data={
    'name':['ron','susu','chauhan','arya'],
    'branch':['ce','ce','extc','ece'],
    'age':[17,18,19,20],
    'marks':[80,90,100,60]
}

df=pd.DataFrame(data)
print(df)
print(df['name'])
print(df[['name','marks']])
df['grade']=['A','B','C','A']
print(df)
print(df.iloc[1:4])
print(df.iloc[:])
print(df[df['age']>18])
print(df['marks'].mean())
print(df.groupby('branch')['marks'].mean())
print(df.columns)
print(df.shape)