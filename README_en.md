#  Asia University CS Professor Crawler

A Python web crawler that extracts professors' names, English names, and research fields from the [official website](https://csie.asia.edu.tw/zh_tw/TeacherIntroduction/Full_time_faculty) of the Department of Computer Science and Information Engineering, Asia University.

---

##  Features

- Extracts professors’ Chinese name, English name, and research areas
- Saves the data into `research_areas.txt`
- Stores the same data into a SQLite database `professors.db`

---

##  How to Run

1. Install dependencies:
   
   pip install requests beautifulsoup4

2. Run the crawler:
   python 期中報告.py

## Output Format

   1. research_areas.txt
      
     Name: 張文鐘（Wen-Thong Chang）
     Research: IoT Systems, Video Streaming, Communication Systems, Image Processing
     ---
     Name: 蔡建發（Jeffrey J.P. Tsai）
     Research: AI, Bioinformatics, Software Engineering, Distributed Real-Time Systems
     ...

   2.  professors.db (SQLite)
   
      CREATE TABLE professors (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       name TEXT,
       eng_name TEXT,
       research_area TEXT
     );

## Technologies Used

  - requests
  - BeautifulSoup
  - sqlite3

## Notes

  - For educational use only. Data sourced from Asia University CSIE’s official website.
