import requests

GROUP_ID = '6057769'
API_KEY = 'ky4BpzcnHwHJ4VUsWb74NPCc'  # Or leave as '' if public

url = f"https://api.zotero.org/groups/{6057769}/items/top?format=json"
headers = {"Zotero-API-Key": API_KEY} if API_KEY else {}

response = requests.get(url, headers=headers)
response.raise_for_status()

items = response.json()

print(f"✅ Retrieved {len(items)} items from Zotero group!")
print(f"First title: {items[0]['data']['title']}")
