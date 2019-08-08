import json
import sys

data = {}

# Load json data
with open(sys.argv[1]) as json_file:
    data = json.load(json_file)

# Parse json data
tickets = data["activities_data"]

# Add activity to short_activity_table
def addShort():
    print("short")

# Add activity to long_activity_table
def addLong():
    print("long")

for ticket in tickets:
    if (ticket["activity_type"]==0):
        addShort()
        print(ticket)
    else:
        addLong()
        print(ticket)
