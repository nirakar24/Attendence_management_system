import sqlite3

db=sqlite3.connect("students.db")

cur_sor = db.cursor()

cur_sor.execute("""CREATE TABLE teachers (
            name text,
            Department text,
            Password text
        )
            """)

# cur_sor.execute("DROP TABLE Attendence")

db.commit()

db.close()
print("Successfully created database")