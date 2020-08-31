import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

url = "https://www.iban.com/currency-codes"
codes = []
exchange = []


def show():
    print("Welcome to CurrencyConvert PRO 2000 \n")
    for num, lst in enumerate(codes):
        print(f"#{num} {lst[0]}")


def get_page():
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')

    for tr in soup.find_all('tr')[1:]:
        td = tr.find_all('td')
        if td[2].text:
            codes.append((td[0].text.capitalize(), td[2].text))


def display_message():
    try:
        print("\nWhere are you from? Choose a country by number.\n")
        num = int(input("#: "))
        if num in range(len(codes)):
            first = codes[num][1]
            exchange.append(first)
            print(codes[num][0] + "\nNow choose another country.")
            another = int(input("#: "))
            if another in range(len(codes)):
                second = codes[another][1]
                exchange.append(second)
                if first != second:
                    print(
                        codes[another][0] + f"\nHow many {exchange[0]} do you want to convert to {exchange[1]}?")
                else:
                    print("The price units of the two countries are the same!")
                    exit()
            else:
                print("Choose a second number from the list \n reset choice.")
                display_message()

        else:
            print("Choose a number from the list")
            display_message()

    except ValueError:
        print("That wasn't a number")
        display_message()


def exchange_system():
    try:
        money = int(input("input money : "))
        exUrl = f"https://transferwise.com/gb/currency-converter/{exchange[0]}-to-{exchange[1]}-rate?amount={money}"
        result = requests.get(exUrl)
        soup = BeautifulSoup(result.content, 'html.parser')
        exMoney = float(
            soup.find("span", {"class": "text-success"}).text)*money
        first = format_currency(money, exchange[0])
        second = format_currency(exMoney, exchange[1])
        print(f"{first} is {second}")
    except:
        print("not supported price units.")
        exit()


def main():
    get_page()
    show()
    display_message()
    exchange_system()


main()
