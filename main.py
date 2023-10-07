# Блок импортов
from requests_html import HTMLSession
import os

# Блок объявления переменных
priceCartRUB = 0.0
priceCartUSD = 0.0
UsdRubConvert = 0.0
textFinder = "RUB"

# Шаг 1 Получаем размер корзины в рублях
priceCartRUB = float(input("Введите размер вашей корзины в рублях используя символ . для десятых и сотых << "))

# Шаг 2 Получаем курс 1 доллар в рублях в стиме
session = HTMLSession()
response = session.get("https://t.me/s/steamrub")
substringID = response.text.rfind(textFinder)
currencyStr = response.text[substringID - 7:substringID - 1]
if currencyStr[0] == " ":
    currencyStr = currencyStr[1:]
UsdRubConvert = float(currencyStr)

# Шаг 3 Вычисляем корзину в долларах
priceCartUSD = priceCartRUB / UsdRubConvert

# Шаг 4 Выводим информацию пользователю
print(f"Текущий курс 1 доллара к рублю >> {UsdRubConvert} RUB/USD\n"
      f"Ваша корзина в рублях >> {priceCartRUB} RUB\n"
      f"Ваша корзина в долларах для Киви >> {priceCartUSD} USD, Округляя до двух знаков  >> {round(priceCartUSD, 2)} $")

os.system("pause")
