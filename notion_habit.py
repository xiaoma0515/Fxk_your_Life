import os
import requests
from datetime import date

# 从环境变量读取 Notion Token 和 Database ID（安全做法）
NOTION_TOKEN = os.environ['NOTION_TOKEN']
DATABASE_ID = os.environ['NOTION_DATABASE_ID']

headers = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28"
}

today = date.today().isoformat()

# 如果你有多个习惯要关联，需要先获取 Habit 的 page_id
# 假设你要关联两个习惯，这里手动填入 Habit 页面 ID
habit_ids = [
    "习惯ID1",  # 替换成你习惯页面的ID
    "习惯ID2"   # 可以加更多
]

data = {
    "parent": {"database_id": DATABASE_ID},
    "properties": {
        "Date": {"date": {"start": today}},
        "Habit": {"relation": [{"id": hid} for hid in habit_ids]},
        "Done": {"checkbox": False}
    }
}

response = requests.post("https://api.notion.com/v1/pages", headers=headers, json=data)
if response.status_code == 200:
    print(f"成功添加 {today} 的打卡行")
else:
    print("添加失败:", response.status_code, response.text)
