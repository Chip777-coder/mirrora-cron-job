
import requests
import json
import os

NOTION_SECRET = os.getenv("NOTION_SECRET")
NOTION_DB_ID = os.getenv("NOTION_DATABASE_ID")

def log_to_notion(repo, event_type, content):
    headers = {
        "Authorization": f"Bearer {NOTION_SECRET}",
        "Content-Type": "application/json",
        "Notion-Version": "2022-06-28",
    }

    data = {
        "parent": {"database_id": NOTION_DB_ID},
        "properties": {
            "Repository": {"title": [{"text": {"content": repo}}]},
            "Event": {"rich_text": [{"text": {"content": event_type}}]},
            "Details": {"rich_text": [{"text": {"content": content}}]},
        },
    }

    response = requests.post("https://api.notion.com/v1/pages", headers=headers, data=json.dumps(data))
    return response.status_code
