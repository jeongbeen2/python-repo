import csv
import requests
import math
from bs4 import BeautifulSoup

front = "http://"
dot = "."
alba_url = "alba.co.kr/job/brand/?page="
page_size = 50
jobPage = input(
    "Plz enter corporation name (ex.kfc, subway, norangtongdak ... ): ")
koreaName = input("What's name you want save? : ")
fake_result = requests.get(f"{front}{jobPage}{dot}{alba_url}")
fake_soup = BeautifulSoup(fake_result.text, 'html.parser')
jobCount = fake_soup.find("p", {"class": "jobCount"}).text.strip("건")
max_page = math.ceil(int(jobCount)/page_size)
page = max_page
jobList = []

for pages in range(page):
    result = requests.get(f"{front}{jobPage}{dot}{alba_url}{pages+1}")
    soup = BeautifulSoup(result.text, 'html.parser')
    tbody = soup.find("tbody")

    for tr in tbody:
        td_place = tr.find("td", {"class": "local"})
        td_title = tr.find("span", {"class": "company"})
        td_data = tr.find("td", {"class": "data"})
        td_pay = tr.find("td", {"class": "pay"})
        td_regDate = tr.find("td", {"class": "regDate"})

        if td_place and td_title and td_data and td_pay and td_regDate:
            jobs = {
                "place": td_place.text.replace(u'\xa0', u' '),
                "title": td_title.text,
                "data": td_data.text,
                "pay": td_pay.text,
                "date": td_regDate.text
            }
            jobList.append(jobs)

    file = open(f"{koreaName}.csv", mode="w", encoding="utf8")
    writer = csv.writer(file)
    writer.writerow(["place", "title", "data", "pay", "date"])
    for job in jobList:
        writer.writerow(list(job.values()))
