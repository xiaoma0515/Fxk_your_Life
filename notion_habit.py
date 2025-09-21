import os
import requests
from datetime import date

# 从 GitHub Secrets 获取 Token 和 Database ID
NOTION_TOKEN = os.environ['NOTION_TOKEN']
DATABASE_ID = os.environ['NOTION_DATABASE_ID']

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

today = date.today().isoformat()  # 例如 '2025-09-21'

# Gym 列关联的页面 ID（需要提前获取 Gym 表中你要关联的页面 ID）
gym_page_ids = [
    "gym-page-id-1",  # 替换成 Gym 表中某个页面的 ID
]

data = {
    "parent": {"database_id": DATABASE_ID},
    "properties": {
        "Day": {"title": [{"text": {"content": "Today"}}]},
        "Date": {"date": {"start": today}},
        "Gym": {"relation": [{"id": gid} for gid in gym_page_ids]},
        "Workout": {"checkbox": False},
        "Checkbox 1": {"checkbox": False},
        "Checkbox 2": {"checkbox": False}
    }
}

response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
if response.status_code == 200:
    print(f"成功添加 {today} 的打卡行")
else:
    print("添加失败:", response.status_code, response.text)
