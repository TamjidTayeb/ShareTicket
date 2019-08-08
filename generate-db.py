import json
import sys
import sqlite3

data = {}

# Load json data
with open(sys.argv[1]) as json_file:
    data = json.load(json_file)

tickets = data["activities_data"]

# Add activity to short_activity_table
def addShort():
    print("short")

# Add activity to long_activity_table
def addLong():
    print("long")

conn = sqlite3.connect("db.sqlite")
c = conn.cursor()

# c.execute(
#     """CREATE TABLE tickets (
#             ticket_id integer,
#             activity_type integer,
#             performer_type text,
#             performer_id integer,
#             performed_at text
#     )"""
# )
c.execute("INSERT INTO tickets VALUES (1,1,'lol',2,'your mum')")
c.execute("SELECT * FROM tickets")
print(c.fetchall())
conn.commit()


# Parse json data
for ticket in tickets:
    if (ticket["activity_type"]==0):
        addShort()
    else:
        addLong()