import sqlite3

con=sqlite3.connect('moviesdatabase.db')
cursorObj=con.cursor()

query_command=""" CREATE TABLE IF NOT EXISTS Movies(name TEXT PRIMARY KEY,actor TEXT,actress TEXT,year INTEGER,director TEXT) """
cursorObj.execute(query_command)

cursorObj.execute(" INSERT INTO Movies VALUES ('Om Shanti Om','Shah Rukh Khan','Deepika Padukone',2007,'Farah Khan')")
cursorObj.execute(" INSERT INTO Movies VALUES ('The Sky Is Pink','Farhan Akhtar','Priyanka Chopra Jonas',2019,'Shonali Bose')")
cursorObj.execute(" INSERT INTO Movies VALUES ('3 Idiots','Aamir Khan','Kareena Kapoor',2009,'Rajkumar Hirani')")
cursorObj.execute(" INSERT INTO Movies VALUES ('Hera Pheri','Akshay Kumar','Tabu',2000,'Priyadarshan')")
cursorObj.execute(" INSERT INTO Movies VALUES ('Interstellar','Matthew McConaughey','Anne Hathaway', 2014,'Christopher Nolan')")
cursorObj.execute(" INSERT INTO Movies VALUES ('Joker','Joaquin Phoenix','Zazie Beetz',2019,'Todd Phillips')")
cursorObj.execute(" INSERT INTO Movies VALUES ('Inception','Leonardo DiCaprio','Elliot Page',2010,'Christopher Nolan')")
cursorObj.execute(" INSERT INTO Movies VALUES ('Five Feet Apart','Cole Sprouse','Haley Lu Richardson',2019,'Justin Baldoni')")

cursorObj.execute("SELECT * FROM Movies")
r1=cursorObj.fetchall()
cursorObj.execute("SELECT * FROM Movies WHERE actor='Cole Sprouse' ")
r2=cursorObj.fetchall()

print(r1)
print(r2)
