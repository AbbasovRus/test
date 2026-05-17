import pandas as pd

df = pd.read_csv('sales.csv')

# 1. Преобразуем дату
df['date'] = pd.to_datetime(df['date'])

# 2. Добавим колонку с выручкой (если еще нет)
df['revenue'] = df['quantity'] * df['price']

# 3. Добавим колонки с частями даты
df['weekday_name'] = df['date'].dt.day_name()
df['month'] = df['date'].dt.month

# 4. Вопросы для анализа
print("=" * 50)
print("АНАЛИЗ ПРОДАЖ ПО ДНЯМ НЕДЕЛИ")
print("=" * 50)

# Выручка по дням недели
revenue_by_weekday = df.groupby('weekday_name')['revenue'].sum()
print(revenue_by_weekday.sort_values(ascending=False))

print("\n" + "=" * 50)
print("ПРОДАЖИ ПО МЕСЯЦАМ")
print("=" * 50)

# Выручка по месяцам
revenue_by_month = df.groupby('month')['revenue'].sum()
print(revenue_by_month)

# 5. Сохраним обогащенный DataFrame
df.to_csv('sales_with_dates.csv', index=False)
print("\nСохранено в sales_with_dates.csv")

# 6. продажи за выходные
weekend_sales = df[(df['date'].dt.dayofweek == 5) | (df['date'].dt.dayofweek == 6)]
print(f"Продажи в выходные: {weekend_sales['revenue'].sum()}")

monday_sales = df[df['weekday_name'] == 'Monday']
print(monday_sales[['date', 'product', 'revenue']])