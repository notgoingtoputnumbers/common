import cs50
import csv
from sys import argv, exit

if len(argv) != 2:
    print("wrong")
    exit(1)

    
db = cs50.SQL("sqlite:///students.db")

db.execute("CREATE TABLE students (first TEXT, middle TEXT, last TEXT, house TEXT, birth NUMERIC)") #id INTEGER AUTOINCREMENT, 

with open(argv[1], "r") as chars:
    reader = csv.DictReader(chars, delimiter = ",")
    
    for row in reader:
        names_list = row["name"].split()
        first = names_list[0]
        last = names_list[-1]
        if len(names_list) == 3:
            middle = names_list[1]
        else:
            middle = "NULL"
        house = row["house"]
        birth = row["birth"]
        
        db.execute("INSERT INTO students (first, middle, last, house, birth) VALUES(?, ?, ?, ?, ?)", first, middle, last, house, birth)


