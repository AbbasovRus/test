import requests
import pandas as pd

# 1. Получаем данные
url = "https://www.cbr-xml-daily.ru/daily_json.js"
response = requests.get(url)
data = response.json()

# 2. Смотрим основные курсы
print("=== КУРСЫ ВАЛЮТ ===")
print(f"Доллар (USD): {data['Valute']['USD']['Value']} ₽")
print(f"Евро (EUR): {data['Valute']['EUR']['Value']} ₽")
print(f"Юань (CNY): {data['Valute']['CNY']['Value']} ₽")
print()

# 3. Создаем DataFrame со всеми валютами
currencies = []
for code, info in data['Valute'].items():
    currencies.append({
        'code': code,
        'name': info['Name'],
        'rate': info['Value'],
        'nominal': info['Nominal']
    })

df = pd.DataFrame(currencies)

# 4. Анализ
print("=== СТАТИСТИКА ===")
print(f"Всего валют: {len(df)}")
print(f"Самая дорогая: {df.loc[df['rate'].idxmax(), 'name']} — {df['rate'].max():.2f} ₽")
print(f"Самая дешевая: {df.loc[df['rate'].idxmin(), 'name']} — {df['rate'].min():.2f} ₽")
print(f"Средний курс: {df['rate'].mean():.2f} ₽")

# 5. Сохраняем
df.to_csv('currency_rates.csv', index=False)
print("\nСохранено в currency_rates.csv")