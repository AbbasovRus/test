import pandas as pd

# 1. Загрузи файл
df = pd.read_csv('shop_sales.csv')

# 2. Посмотри первые 5 строк
print("Первые 5 строк:")
print(df.head())

# 3. Выведи информацию о данных (типы, пропуски)
print("\nИнформация:")
print(df.info())

# 4. Преобразуй колонку date в datetime
df['date'] = pd.to_datetime(df['date'])

# 5. Добавь колонку revenue = quantity * price
df['revenue'] = df['quantity'] * df['price']

# 6. Добавь колонки month и weekday_name
df['month'] = df['date'].dt.month
df['weekday_name'] = df['date'].dt.day_name()

print(df.head())

# Общая выручка магазина
total_revenue = df['revenue'].sum()
print(f'Общая выручка магазина {total_revenue}')

# Товар, принесший больше всего выручки
product_revenue = df.groupby('product')['revenue'].sum()
best_product = product_revenue.idxmax()  # название товара
best_product_value = product_revenue.max()  # сумма
print(f'товар с максимальной выручкой: {best_product}, он принес: {best_product_value} рублей')

# Кол-во продаж в Москве
msc_sales = df[df['city'] == 'Москва']['quantity'].sum()
print(f'В Москве было {msc_sales} продаж')

# Месяц, который принес наибольшую выручку
month_revenue = df.groupby('month')['revenue'].sum()
best_month = month_revenue.idxmax()
print (f'Самый лучший месяц {best_month}')

# Самый прибыльный день недели
day_revenue = df.groupby('weekday_name')['revenue'].sum()
best_day = day_revenue.idxmax()
print (f'Самый лучший день {best_day}')

# Средняя выручка за одну продажу
avg_revenue = df['revenue'].mean()
print(f'Средний чек магазина {avg_revenue}')

# Топ 3 продажи по выручке
top_3 = df.sort_values('revenue', ascending=False).head(3)
print(top_3[['date','product','revenue']])

# Выручка по категориям
category_revenue = df.groupby('category')['revenue'].sum()
category_revenue_sorted = category_revenue.sort_values(ascending=False)
print(category_revenue_sorted)

df.to_csv('shop_analysis.csv', index=False)