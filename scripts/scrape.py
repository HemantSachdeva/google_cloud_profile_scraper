import pandas as pd
import requests
from bs4 import BeautifulSoup

data = pd.read_csv("data/input.csv")
rows = []

for row in data.itertuples():
    name = row.name
    profile_url = row.profile_url
    response = requests.get(profile_url)
    soup = BeautifulSoup(response.text, "html.parser")

    badges = soup.select(".ql-subhead-1")

    d = {"name": name, "badges": ""}
    for index, item in enumerate(badges):
        title = badges[index].getText().replace("\n", "")
        d["badges"] += f"{title}, "

    rows.append(d)

header = ["Name", "Badges"]
df = pd.DataFrame.from_dict(rows)
df.to_csv(path_or_buf="data/output.csv", header=header)