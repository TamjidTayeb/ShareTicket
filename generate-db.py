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
    return 1
    print("short")

# Add activity to long_activity_table
def addLong():
    return 1
    print("long")

conn = sqlite3.connect("db.sqlite")
c = conn.cursor()

c.execute(
    """CREATE TABLE IF NOT EXISTS tickets (
            ticket_id integer PRIMARY KEY,
            activity_type integer,
            performer_type text,
            performer_id integer,
            performed_at text
    )"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS short_activities (
            ticket_id integer references tickets(ticket_id) PRIMARY KEY,
            note_id integer,
            note_type integer
    )"""
)

c.execute(
    """CREATE TABLE IF NOT EXISTS long_activities (
            ticket_id integer references tickets(ticket_id) PRIMARY KEY,
            agent_id integer,
            status text,
            requester integer,
            product text,
            contacted_customer BOOLEAN,
            category text,
            group_of text,
            priority integer,
            source integer,
            shipment_date text,
            issue_type text,
            shipping_address text
    )"""
)
# c.execute("DROP TABLE long_activities")
c.execute("SELECT * FROM long_activities")
print(c.fetchall())
c.execute("SELECT * FROM short_activities")
print(c.fetchall())
c.execute("SELECT * FROM tickets")
print(c.fetchall())
conn.commit()


# Parse json data
for ticket in tickets:
    if (ticket["activity_type"]==0):
        addShort()
    else:
        addLong()