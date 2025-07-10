import requests
import os
from datetime import datetime

GROUP_ID = '6057769'
API_KEY = 'ky4BpzcnHwHJ4VUsWb74NPCc'

ZOTERO_API_URL = f"https://api.zotero.org/groups/{GROUP_ID}/items/top?format=json"
HEADERS = {"Zotero-API-Key": API_KEY} if API_KEY else {}

def fetch_publications():
    response = requests.get(ZOTERO_API_URL, headers=HEADERS)
    response.raise_for_status()
    return response.json()

def format_html(items):
    html = "<ul>\n"
    for item in items:
        data = item['data']
        title = data.get('title', '[Untitled]')
        year = data.get('date', '')[:4]
        creators = data.get('creators', [])
        authors = ', '.join(
            f"{c.get('lastName', '')}" for c in creators if c.get('creatorType') == 'author'
        )
        url = data.get('url') or data.get('DOI')
        if url and not url.startswith('http'):
            url = f"https://doi.org/{url}"

        citation = f"{authors} ({year}). <i>{title}</i>"

        if url:
            citation = f"<a href='{url}' target='_blank'>{citation}</a>"

        html += f"  <li>{citation}</li>\n"
    html += "</ul>"
    return html

def save_html(html):
    os.makedirs("data", exist_ok=True)
    with open("data/publications.html", "w", encoding="utf-8") as f:
        f.write(f"<!-- Auto-generated on {datetime.now().isoformat()} -->\n")
        f.write(html)
    print("✅ Saved to data/publications.html")

def main():
    items = fetch_publications()
    html = format_html(items)
    save_html(html)

if __name__ == "__main__":
    main()
