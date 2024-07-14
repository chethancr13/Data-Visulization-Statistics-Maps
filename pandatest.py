import pandas as pd
import matplotlib.pyplot as plt


data = {'City': ['New York', 'Los Angeles', 'Chicago'],
        'Jan': [100, 80, 60],
        'Feb': [120, 90, 70],
        'Mar': [110, 100, 80]}
df = pd.DataFrame(data)


plt.figure(figsize=(10, 6))
df.plot(kind='bar', stacked=True, x='City')
plt.xlabel('City')
plt.ylabel('Sales')
plt.title('Monthly Sales by City (Stacked)')
plt.legend(title='Month')  
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


plt.figure(figsize=(8, 8))
plt.pie(df.iloc[0, 1:], labels=df.columns[1:], autopct="%1.1f%%", hole=0.4)
plt.title('Sales Distribution in New York (Jan-Mar)')
plt.tight_layout()
plt.show()


