import sqlite3
con = sqlite3.connect("daum.db")
cur = con.cursor()

# sql = "CREATE TABLE daum_news (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT, link TEXT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"


sql = "INSERT INTO daum_news VALUES(1 , 'news','http://','')"
cur.execute(sql)
con.commit()

