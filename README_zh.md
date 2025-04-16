# 亞洲大學資工系教授資料爬蟲

這是一個使用 Python 撰寫的爬蟲工具，從亞洲大學資訊工程學系的 [官方網站](https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_faculty) 擷取教授的姓名、英文姓名與研究領域，並將資料儲存為文字檔與 SQLite 資料庫。

---

## 功能

- 擷取教授中文姓名、英文姓名與研究領域
- 將資料寫入文字檔 `research_areas.txt`
- 同步寫入 SQLite 資料庫 `professors.db`

---

## 執行方式

1. 安裝必要套件：

   pip install requests beautifulsoup4
   
3. 執行爬蟲：

   python 期中報告.py

## 輸出格式

   1. research_areas.txt
      
      姓名：張文鐘（Wen-Thong Chang）
      研究領域：物連網系統、視訊串流、通訊系統、影像處理
      ---
      姓名：蔡建發（Jeffrey J.P. Tsai）
      研究領域：人工智慧、生物資料、軟體工程、分散式即時系統
      ...
   
   2. professors.db（SQLite）
   
      CREATE TABLE professors (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          name TEXT,
          eng_name TEXT,
          research_area TEXT
      );

## 使用技術

   - requests
   - BeautifulSoup
   - sqlite3

## 注意事項

   - 本專案僅供課堂與學術用途，資料來源為亞洲大學資工系官方網站

