import requests

print("Welcome to IsItDown.py!")

while True:
    print("Please write a URL or URLs you want to check. (seperated by comma.)")

    front = "https://"
    backs = (".com", ".net", ".co", ".kr")
    inputUrl = input().split(",")

    for urls in inputUrl:
        url = urls.strip()

        try:
            if url.startswith(front) == True:
                response = requests.get(url)

                if response.status_code == 200:
                    print(f"{url} is up!")

            elif url.startswith(front) != True:
                newUrl = front+url

                if newUrl.endswith(backs) == True:
                    response = requests.get(newUrl)

                    if response.status_code == 200:
                        print(f"{front}{url} is up!")

                else:
                    print(f"{url} is not a valid url.")

        except:
            print(f"{url} is down!")

    while True:
        choice = input("Do you want to start over? Y/N :")
        if choice == "y" or choice == "Y":
            break

        elif choice == "n" or choice == "N":
            exit()

        else:
            print("That's not a valid answer")
