import os
import requests
from datetime import date, datetime

# 从 GitHub Secrets 获取 Token 和 Database ID
NOTION_TOKEN = os.environ['NOTION_TOKEN']
DATABASE_ID = os.environ['NOTION_HABITTRACKER_DATABASE_ID']

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

today = date.today().isoformat()  # 例如 '2025-09-21'
weekday = datetime.today().weekday()  # 0=周一, 1=周二, ..., 6=周日

# 根据星期几选择 Gym page_id
if weekday == 0:  # 周一
    gym_page_ids = ["27519fe696fa801fa375d97eaf7105e8"]
elif weekday == 2:  # 周三
    gym_page_ids = ["27519fe696fa8001b9c0c407d30dfde8"]
elif weekday == 4:  # 周五
    gym_page_ids = ["27519fe696fa8060925ad8a87d58b2e4"]
elif weekday == 6:  # 周日
    gym_page_ids = ["27519fe696fa80b18073d5e08b18588b"]
else:  # 其他日子
    gym_page_ids = ["27519fe696fa8020ac72c260ecdc428c"]

data = {
    "parent": {"database_id": DATABASE_ID},
    "icon": {"type": "emoji", "emoji": "✅"},
    "properties": {
        "Tracker": {"title": [{"text": {"content": ""}}]},
        "Date": {"date": {"start": today}},
        "Gym": {"relation": [{"id": gid} for gid in gym_page_ids]},
        "Workout": {"checkbox": False},
        "Duolingo": {"checkbox": False},
        "Meditation": {"checkbox": False}
    }
}

response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
if response.status_code == 200:
    print(f"成功添加 {today} 的打卡行")
else:
    print("添加失败:", response.status_code, response.text)
