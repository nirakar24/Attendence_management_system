import sqlite3

db=sqlite3.connect("students.db")

cur_sor = db.cursor()

cur_sor.execute("""CREATE TABLE Attendence (
            name text,
            roll_no integer,
            Department text,
            Password text,
            present integer,
            absent integer
        )
            """)

# cur_sor.execute("DROP TABLE Attendence")

db.commit()

db.close()
print("Successfully created database")