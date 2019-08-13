import json
import sys
import sqlite3

data = {}

# Load json data
with open(sys.argv[1]) as json_file:
    data = json.load(json_file)

tickets = data["activities_data"]

conn = sqlite3.connect("db.sqlite")
c = conn.cursor()

# Add activity to short_activity_table
def addShort(ticket):
    activity = ticket["activity"]
    note = activity["note"]

    ticketId = ticket["ticket_id"]
    noteType = note["type"]
    noteId = note["id"]

    c.execute(
        "INSERT INTO short_activities VALUES (?,?,?)", 
        (ticketId,noteType,noteId)
    )

# Add activity to long_activity_table
def addLong(ticket):
    activity = ticket["activity"]
    ticketId = ticket["ticket_id"]
    agentId = activity["agent_id"]
    status = activity["status"]
    requester = activity["requester"]
    product = activity["product"]
    contactedCustomer = activity["contacted_customer"]
    category = activity["category"]
    groupOf = activity["group"]
    priority = activity["priority"]
    source = activity["source"]
    shipmentDate = activity["shipment_date"]
    issueType = activity["issue_type"]
    shipping_address = activity["shipping_address"]
    c.execute(
        "INSERT INTO long_activities VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", 
        (ticketId, agentId, status,requester,product,contactedCustomer,category,groupOf,priority,source,shipmentDate,issueType,shipping_address)
    )

def addBasic(ticket):
    ticketId = ticket["ticket_id"]
    activityType = ticket["activity_type"]
    performerType = ticket["performer_type"]
    performerId = ticket["performer_id"]
    performedAt = ticket["performed_at"]
    c.execute(
        "INSERT INTO tickets VALUES (?,?,?,?,?)",
        (ticketId,activityType,performerType,performerId,performedAt)
    )


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
        addBasic(ticket)
        addShort(ticket)
    else:
        addBasic(ticket)
        addLong(ticket)
c.execute("SELECT * FROM short_activities")
print(c.fetchall())
c.execute("SELECT * FROM long_activities")
print(c.fetchall())
c.execute("SELECT * FROM tickets")
print(c.fetchall())
# conn.commit()