1 Create a new database with a table named Roster that has three fields: Name, Species, and Age. The Name and Species columns should be text fields, and the Age column should be an integer field.
import sqlite3

with sqlite3.connect('homework.db') as conn:
    cursor = conn.cursor()
    sql_query = 'create table Roster (Name varchar(30), Species varchar(50), Age int)'
    cursor.execute(sql_query)
2 Populate your new table with the following values:
with sqlite3.connect('homework.db') as conn:
    cursor = conn.cursor()
    insert_query = """insert into Roster values ('Benjamin Sisko', 'Human', 40),
                                                ('Jadzia Dax', 'Trill',300 ),
                                                ('Kira Nerys', 'Bajoran', 29)"""
    cursor.execute(insert_query)
3 Update the Name of Jadzia Dax to be Ezri Dax
with sqlite3.connect('homework.db') as conn:
    cursor = conn.cursor()
    update_query = """update Roster
                      set Name = 'Ezri Dax'
                       where Name = 'Jadzia Dax'"""
    cursor.execute(update_query)
4 Display the Name and Age of everyone in the table classified as Bajoran.
with sqlite3.connect('homework.db') as conn:
    cursor = conn.cursor()
    sql_query = """select Name, age from Roster
                    where Species = 'Bajoran'"""
    result = cursor.execute(sql_query)
    print(result.fetchall())
