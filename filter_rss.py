import feedparser
from feedgen.feed import FeedGenerator
import os
import re

# Define the RSS feed URL
RSS_URL = "https://www.uleth.ca/notice/rss/all"
DEPARTMENT_ID = "344"  # Change this to the department code you need
DEPARTMENT_FILTER_PATTERN = f"/notice/filter/{DEPARTMENT_ID}"

# Parse the RSS feed
feed = feedparser.parse(RSS_URL)

# Create a new RSS feed generator
fg = FeedGenerator()
fg.title(f"Filtered U of L Notices - Department {DEPARTMENT_ID}")
fg.link(href=RSS_URL)
fg.description(f"Filtered notices for Department {DEPARTMENT_ID}")

# Filter entries where department ID appears in the description
for entry in feed.entries:
    if DEPARTMENT_FILTER_PATTERN in entry.description:
        fe = fg.add_entry()
        fe.title(entry.title)
        fe.link(href=entry.link)
        fe.description(entry.description)
        fe.pubDate(entry.published)

# Generate the new RSS XML file
output_path = "docs/filtered_feed.xml"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "wb") as f:
    f.write(fg.rss_str(pretty=True))

print("Filtered RSS feed generated successfully!")
