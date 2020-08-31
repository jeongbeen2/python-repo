import os
import requests
from bs4 import BeautifulSoup

os.system("clear")
url = "https://www.iban.com/currency-codes"
codes = []


def show():
    print("Hello! Please choose a country by selecting a number.")
    for num, lst in enumerate(codes):
        print(f"# {num} {lst[0]}")


def get_page():
    result = requests.get(url)
    soup = BeautifulSoup(result.content, 'html.parser')

    for tr in soup.find_all('tr')[1:]:
        td = tr.find_all('td')
        if td[2].text:
            codes.append((td[0].text.capitalize(), td[2].text))


def display_message():
    try:
        num = int(input("#: "))
        if num in range(len(codes)):
            print(f"The currency code for {codes[num][0]} is {codes[num][1]}")
            again = input("Try again? y/n : ")

            while True:
                if again == "y":
                    display_message()
                elif again == "n":
                    print("Thank you!")
                    exit()
                else:
                    print("you should put in 'y' or 'n'")
                    break

        else:
            print("Choose a number from the list")
            display_message()

    except ValueError:
        print("That wasn't a number")
        display_message()


def main():
    get_page()
    show()
    display_message()


main()
