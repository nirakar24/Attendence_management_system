import sqlite3

db=sqlite3.connect("students.db")

cur_sor = db.cursor()

cur_sor.execute("""CREATE TABLE Attendence (
            name text,
            Roll_no INT,
            Branch text,
            password text,
            present int,
            absent int
        )
            """)

# cur_sor.execute("DROP TABLE Attendence")

db.commit()

db.close()
print("Successfully created database")