import json
import sys
import random
from datetime import timedelta, datetime
from random import randrange

#Raise exception when script not run in correct format
if (len(sys.argv)!=3):
    raise Exception('Please input the number of activities and filename to save to as paramaters in order to run this script. Follow this format: generate-tickets 1000 myjsonfile.json')

#Array of activities
activities = []
activitiesCount = int(sys.argv[1])
#Start and End Time
d1 = '1/1/2017 12:00 AM'
d2 = '2/1/2018 11:59 PM'
#All possible column values
performerTypes = ["user","admin","service worker"]
categories = ["Phone","Web","Walk in"]
issueTypes = ["incident","complaint","enquiry"]
statusses = ["Open","Closed","Resolved","Waiting for Customer","Waiting for Third Party","Pending"]
groups = ["refund","recall","purchase"]
products = ["mobile","laptop","desktop","monitor","mouse","keyboard"]
adresses = [
  "777 Brockton Avenue, Abington MA 2351",
  "30 Memorial Drive, Avon MA 2322",
  "250 Hartford Avenue, Bellingham MA 2019",
  "700 Oak Street, Brockton MA 2301",
  "66-4 Parkhurst Rd, Chelmsford MA 1824",
  "591 Memorial Dr, Chicopee MA 1020",
  "55 Brooksby Village Way, Danvers MA 1923",
  "137 Teaticket Hwy, East Falmouth MA 2536",
  "42 Fairhaven Commons Way, Fairhaven MA 2719",
  "374 William S Canning Blvd, Fall River MA 2721",
  "121 Worcester Rd, Framingham MA 1701",
  "677 Timpany Blvd, Gardner MA 1440",
  "337 Russell St, Hadley MA 1035",
  "295 Plymouth Street, Halifax MA 2338",
  "1775 Washington St, Hanover MA 2339",
  "280 Washington Street, Hudson MA 1749",
  "20 Soojian Dr, Leicester MA 1524",
  "11 Jungle Road, Leominster MA 1453",
  "301 Massachusetts Ave, Lunenburg MA 1462",
  "780 Lynnway, Lynn MA 1905",
  "70 Pleasant Valley Street, Methuen MA 1844",
  "830 Curran Memorial Hwy, North Adams MA 1247",
  "1470 S Washington St, North Attleboro MA 2760",
  "506 State Road, North Dartmouth MA 2747",
  "742 Main Street, North Oxford MA 1537"
  ]
#Arrays of different ids
agentIds = []
ticketIds = []
performerIds = []
noteIds = []


# from https://stackoverflow.com/a/553448
def randomDate(startDate, endDate):
   """
   This function will return a random datetime between two datetime
   objects.
   """
   start = datetime.strptime(startDate, '%d/%m/%Y %I:%M %p')
   end = datetime.strptime(endDate, '%d/%m/%Y %I:%M %p')
   delta = end - start
   intDelta = (delta.days * 24 * 60 * 60) + delta.seconds
   randomSecond = randrange(intDelta)
   return datetime.strftime(start + timedelta(seconds=randomSecond), '%d-%m-%Y %H:%M:%S +0000')

def generateID(array):
    while True:
        id = random.randint(1,1000)
        if id not in array:
            break
    array.append(id)
    return id


def generateShortActivity():
    a = {
            "performed_at":randomDate(d1,d2),
            "ticket_id":generateID(ticketIds),
            "performer_type":random.choice(performerTypes),
            "performer_id":generateID(performerIds),
            "activity": {
                "note": {
                    "id": generateID(noteIds),
                    "type": random.randint(1,10)
                }
        }
    }
    return a

def generateLongActivity():
    a = {
            "performed_at":randomDate(d1,d2),
             "ticket_id":generateID(ticketIds),
             "performer_type":random.choice(performerTypes),
             "performer_id":generateID(performerIds),
            "activity":{
                "shipping_address":random.choice(adresses),
                "shipment_date":randomDate(d1,d2),
                "category":random.choice(categories),
                "contacted_customer":bool(random.getrandbits(1)),
                "issue_type":random.choice(issueTypes),
                "source":random.randint(1,15),
                "status":random.choice(statusses),
                "priority":random.randint(1,4),
                "group":random.choice(groups),
                "agent_id":generateID(agentIds),
                "requester":random.randint(1,2000),
                "product":random.choice(products)
            }
    }
    return a

#Generating activities data in list of dicts
for i in range(activitiesCount):
    longOrShort = random.randint(0,1)
    if (longOrShort==0):
        activity = generateLongActivity()
    else:
        activity = generateShortActivity()
    activities.append(activity)

#Generating and assembling JSON data
data = {
    "metadata":{
      "start_at": d1+" + 0000",
      "end_at": d2+" + 0000",
      "activities_count": activitiesCount
    },
    "activities_data": activities
}

#save json data to file provided in command line
with open(sys.argv[2], 'w') as f:
       json.dump(data, f)

# Print resulting JSON:
y = json.dumps(data)
print(y)