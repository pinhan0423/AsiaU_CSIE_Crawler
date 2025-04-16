import requests
from bs4 import BeautifulSoup

url = 'https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_faculty'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')

teachers = soup.find_all('div', class_='i-member-item')

for teacher in teachers:
    name_tag = teacher.select_one('.member-data-value-name a')
    name = name_tag.get_text(strip=True) if name_tag else '未提供姓名'

    expertise_tag = teacher.select_one('.member-data-value-7')
    expertise = expertise_tag.get_text(strip=True) if expertise_tag else '未提供研究領域'

    print(f'姓名：{name}')
    print(f'研究領域：{expertise}')
    print('---')

import sqlite3

data = [] 
blocks = soup.find_all("div", class_="i-member-item")

for block in blocks:
    try:
        name_block = block.find("span", class_="member-data-value-name")
        name_text = name_block.get_text(strip=True)

        if "(" in name_text and ")" in name_text:
            name = name_text.split("(")[0].strip()
            eng_name = name_text.split("(")[1].replace(")", "").strip()
        else:
            name = name_text
            eng_name = ""

        research_block = block.find("span", class_="member-data-value-7")
        research_area = research_block.get_text(strip=True) if research_block else ""

        data.append({
            "name": name,
            "eng_name": eng_name,
            "research_area": research_area
        })

    except Exception as e:
        print("跳過一筆資料，因為發生錯誤：", e)

with open("research_areas.txt", "w", encoding="utf-8") as f:
    for prof in data:
        f.write(f"姓名：{prof['name']}（{prof['eng_name']}）\n")
        f.write(f"研究領域：{prof['research_area']}\n")
        f.write("---\n")

print("已寫入 research_areas.txt")

conn = sqlite3.connect("professors.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS research_areas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        eng_name TEXT,
        research_area TEXT
    )
""")

for prof in data:
    cursor.execute("""
        INSERT INTO research_areas (name, eng_name, research_area)
        VALUES (?, ?, ?)
    """, (prof["name"], prof["eng_name"], prof["research_area"]))

conn.commit()
conn.close()

print("已存入 SQLite 資料庫 professors.db")
