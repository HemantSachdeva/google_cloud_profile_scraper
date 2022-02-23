from re import sub

import pandas as pd
import requests
from bs4 import BeautifulSoup

data = pd.read_csv("data/input.csv")
rows = []

VALID_BADGES = [
    "Google Cloud Essentials",
    "Flutter Essentials",
    "Flutter Development",
    "Dart Essentials"
]

for row in data.itertuples():
    name = row.name
    profile_url = row.profile_url
    response = requests.get(profile_url)
    soup = BeautifulSoup(response.text, "html.parser")

    badges = soup.select(".ql-subhead-1")

    d = {"name": name, "badges": ""}
    for index, item in enumerate(badges):
        title = badges[index].getText().replace("\n", "")
        if title in VALID_BADGES:
            d["badges"] += f"{title}, "

    rows.append(d)

for row in rows:
    # remove trailing comma with a space
    row["badges"] = sub(pattern=", $", repl="", string=row["badges"])
    # count of badges to be earned yet
    if len(row["badges"]):
        row["badges_left"] = len(VALID_BADGES) - len(row["badges"].split(","))
    else:
        row["badges_left"] = 4

header = ["Name", "Badges", "Badges left count"]
df = pd.DataFrame.from_dict(rows)
df.to_csv(path_or_buf="data/output.csv", header=header)
