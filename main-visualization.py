# visual representation 
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('sales_data.csv')

category_sales = df.groupby('Category')['Sales'].sum()
print('category_sales,', category_sales)

color_map = {
    'Accessories':'pink',
    'Computers':'blue',
    'Mobiles':'yellow',
}

colors = []

for category in category_sales.index:
    colors.append(color_map[category])

category_sales.plot(kind='bar', color=colors)
plt.title('Catergory Sales')
plt.xlabel('Category')
plt.ylabel('Sales')
plt.show()
