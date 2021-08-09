import sqlite3

con=sqlite3.connect('moviesdatabase.db')
cursor=con.cursor()

query_command=""" CREATE TABLE IF NOT EXISTS Movies(name TEXT PRIMARY KEY,actor TEXT,actress TEXT,year INTEGER,director TEXT) """
cursor.execute(query_command)

cursor.execute(" INSERT INTO Movies VALUES ('Om Shanti Om','Shah Rukh Khan','Deepika Padukone',2007,'Farah Khan')")
cursor.execute(" INSERT INTO Movies VALUES ('The Sky Is Pink','Farhan Akhtar','Priyanka Chopra Jonas',2019,'Shonali Bose')")
cursor.execute(" INSERT INTO Movies VALUES ('3 Idiots','Aamir Khan','Kareena Kapoor',2009,'	Rajkumar Hirani')")
cursor.execute(" INSERT INTO Movies VALUES ('Hera Pheri','Akshay Kumar','Tabu',2000,'Priyadarshan')")
cursor.execute(" INSERT INTO Movies VALUES ('Interstellar','Matthew McConaughey','Anne Hathaway', 2014,'Christopher Nolan')")
cursor.execute(" INSERT INTO Movies VALUES ('Joker','Joaquin Phoenix','Zazie Beetz',2019,'Todd Phillips')")
cursor.execute(" INSERT INTO Movies VALUES ('Inception','Leonardo DiCaprio','Elliot Page',2010,'Christopher Nolan')")
cursor.execute(" INSERT INTO Movies VALUES ('Five Feet Apart','Cole Sprouse','Haley Lu Richardson',2019,'Justin Baldoni')")

cursor.execute("SELECT * FROM Movies")
r1=cursor.fetchall()
cursor.execute("SELECT * FROM Movies WHERE actor='Cole Sprouse' ")
r2=cursor.fetchall()

print(r1)
print(r2)
