
import pandas as pd

from sklearn.preprocessing import LabelEncoder

# data_frame = pd.read_csv('customer_purchase_data.csv')
data_frame = pd.read_csv('sales_data.csv')

# print(data_frame.head())

print(data_frame.tail())

# print(data_frame.info())

# print(data_frame.describe())

# It gives total now of rows and columns
print('Shape :',data_frame.shape)

print(data_frame.columns)

# Prints data types
print('Data types')
print(data_frame.dtypes)

print(data_frame.isna().sum())

print('Customer age mean:')
print(data_frame['Customer_Age'].mean())

print('Quantity mean')
print(data_frame['Quantity'].mean())

print('Rating remove null')
data_frame['Rating'] = data_frame['Rating'].fillna(data_frame['Rating'].mean)

data_frame['Region'] = data_frame['Region'].fillna(data_frame['Region'].mode()[0])

data_frame['Customer_Age'] = data_frame['Customer_Age'].fillna(data_frame['Customer_Age'].mean())

# print(data_frame.isna().sum())

# print(data_frame.head(10))

print('duplicate removes count')
print(data_frame.duplicated().sum())

data_frame = data_frame.drop_duplicates()

print('after duplicate removes count')
print(data_frame.duplicated().sum())

print('Uqnique Gender')
print(data_frame['Gender'].unique())

print('Gender strip method if any whitespaces')
data_frame['Gender'] = data_frame['Gender'].str.strip()

print('Uqnique Gender after')
print(data_frame['Gender'].unique())

print('Gender lower method')
data_frame['Gender'] = data_frame['Gender'].str.lower()
print(data_frame['Gender'].unique())

print(data_frame.isna().sum())

print('Uqnique Region')
print(data_frame['Region'].unique())

print('Gender lower method')
data_frame['Region'] = data_frame['Region'].str.lower()
print(data_frame['Region'].unique())

print(data_frame.columns)

print('Product uinique')
# data_frame['Product'] = data_frame['Product'].unique()
print(data_frame['Product'].unique())

print("Encouder")
label = LabelEncoder()

data_frame['Gender'] = label.fit_transform(data_frame['Gender'])


# analyse the data

category_sales_sum = data_frame.groupby('Category')['Sales'].sum()

print('category_sales_sum:',category_sales_sum)

print('---------------------------')

data_frame['Gst'] = (
    data_frame['Sales'] * 10/100

)
print('Sales :',data_frame['Sales'])

print('Gst:', data_frame['Gst'])


# print('Print a sales more than 10k in chennai')
# print('Chennai region')
# print(data_frame['Region'] == 'Bangalore')
# print('Sales')
# print(data_frame[(data_frame['Sales'] > 1000)])
# result = data_frame[(data_frame['Region'] == 'Chennai') & (data_frame['Sales']>100000)]

# result = data_frame[(data_frame['Region'] == 'Chennai') & (data_frame['Sales']>100000)]
# print(result)

sort_sales = data_frame.sort_values('Sales', ascending=False)
print(sort_sales.head())

print(data_frame['Category'].value_counts())