#!/bin/bash

# Update python script and student records from main branch
rm scripts/scrape.py data/input.csv
curl -L https://raw.githubusercontent.com/HemantSachdeva/google_cloud_profile_scraper/main/scripts/scrape.py >scripts/scrape.py
curl -L https://raw.githubusercontent.com/HemantSachdeva/google_cloud_profile_scraper/main/data/input.csv >data/input.csv
python3 scripts/scrape.py
echo "Last update: $(date)">data/update.log
