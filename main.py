import sqlite3


# Creating a sqlite database to store movie details
movie=sqlite3.connect('movies.db') 

mv=movie.cursor()



#Creating "movies" table
mv.execute('''CREATE TABLE Movies (
    name TEXT PRIMARY KEY NOT NULL,
    actor TEXT,
    actress TEXT,
    director TEXT NOT NULL,
    year_of_release INT NOT NULL );''')



#Inserting data into Movies table
mv.execute("INSERT INTO Movies VALUES('Inception','Leonardo DiCaprio','Marion Cotillard','Christopher Nolan',2010);")
mv.execute("INSERT INTO Movies VALUES('Interstellar','Matthew McConaughey','Anne Hathaway','Christopher Nolan',2014);")
mv.execute("INSERT INTO Movies VALUES('Jumanji: The Next Level','Dwayne Johnson','Karen Gillan','Jake Kasdan',2019);")
mv.execute("INSERT INTO Movies VALUES('Central Intelligence','Dwayne Johnson','','Rawson Marshall Thurber',2016);")
mv.execute("INSERT INTO Movies VALUES('Lucy','','Scarlett Ingrid Johansson','Luc Besson',2014);")
mv.execute("INSERT INTO Movies VALUES('The Fast and the Furious: Tokyo Drift','Lucas Black','Nathalie Kelley','Justin Lin',2006);")




#Querying data from Movies table

#Retrieve all data from table
mv.execute("SELECT * FROM movies;")  
print(mv.fetchall())


#Retrieve all movies name starred by actor Dwayne Johnson
mv.execute("SELECT name FROM movies WHERE actor='Dwayne Johnson';")
print(mv.fetchall())


#Retrieve movies realesed between 2015 to 2020 in ascending order of year of release
mv.execute("SELECT * FROM movies WHERE year_of_release BETWEEN 2015 AND 2020 ORDER BY year_of_release;")
print(mv.fetchall())




movie.commit()
movie.close()
