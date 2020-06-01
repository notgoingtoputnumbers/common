import cs50
from sys import argv, exit

if len(argv) != 2:
    print("wrong")
    exit(1)

db = cs50.SQL("sqlite:///students.db")

rows = db.execute("select id, first, middle, last, birth from students where house = ?", argv[1])
students = dict()
for row in rows:
    students[row['id']] = (row['first'], row['middle'], row['last'], row['birth'])
for val in sorted(students.values(), key = lambda i: (i[2], i[0])):
    if val[1] != "NULL":
        print(val[0], val[1], val[2] + ",", "born", val[3])
    else:
        print(val[0], val[2] + ",", "born", val[3])

        