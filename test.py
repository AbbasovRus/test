import pandas as pd

df = pd.read_csv('sales.csv')

#Выручка
df['revenue'] = df['quantity'] * df['price']

# Общая выручка
print(df['revenue'].sum())

# Товар с максимальной выручкой
product_revenue = df.groupby('product')['revenue'].sum()
best_product = product_revenue.idxmax()  # название товара
best_product_value = product_revenue.max()  # сумма
print(f'товар с максимальной выручкой: {best_product}, он принес: {best_product_value} рублей')

# Продажи в Москве
moscow_sales = len(df[df['customer_city'] == 'Москва'])
print(f'кол-во продаж в Москве: {moscow_sales}')

# Средний чек
avg_chek = df['revenue'].mean()
print(f'Средний чек продаж {avg_chek}')

# Самый лучший день
daily_revenue = df.groupby('date')['revenue'].sum()
best_day = daily_revenue.idxmax()
best_day_revenue = daily_revenue.max()
print(f'В самый лучший день {best_day} заработали {best_day_revenue}')

# Категория с наибольшой выручкой
category_revenue = df.groupby('category')['revenue'].sum()
best_category = category_revenue.idxmax()
print(f'категория с наибольшей выручкой: {best_category}')

# Сортировка и топ 3
top_3 = df.sort_values('revenue', ascending=False).head(3)
print(top_3)

df.to_csv('sales_analysis.csv', index=False)