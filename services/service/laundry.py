import urllib2, urllib
from bs4 import BeautifulSoup

#### Links us to data.py in order to allow us to edit the data therein
import data

#### Title will need to be changed later, though the imports will not

#############################
##    Our Function     ##
#############################    

#### Here's the scraping portion, luckily they've built a lot of it for us
def getMachines(roomid, machinetype):
#### Creates an empty array called 'machines'
    machines = []

#### How will multiple urls work for us, and will we need more than one?
    url = '[PLACEURLTOSCRAPEHERE]'
    
#### Make the url customizable using the roomid
    url += 'cell=null&lr=%s&monitor=true' % (roomid)

#### Create a website object for BeautifulSoup to parse out
    website = urllib2.urlopen(url)

#### Parse out the website using Beautiful Soup
    soup = BeautifulSoup(website.read(), 'html.parser')

#### Find a specific tag using the id that was passed as 'machinetype'
    washer_div = soup.find(id=machinetype)

#### Adjust the array to hold something
#### (I'll have to figure this out a little better)
    machine = washer_div.next_sibling

#### We can investigate the data files to see what exactly this is doing
    if machinetype == 'washer':
        while 'id' not in machine.attrs or machine['id'] != 'dryer':
            machines.append({'lr': roomid,
             'id': machine.a['id'],
             'name': `(machine.a.text)`.split('\\xa0')[0][2:],
             'time': machine.a.p.text})
            machine = machine.next_sibling
    else:
        while machine and machine.name == 'li':
            machines.append({'lr': roomid,
             'id': machine.a['id'],
             'name': `(machine.a.text)`.split('\\xa0')[0][2:],
             'time': machine.a.p.text})
            machine = machine.next_sibling
#### Returns to us the edited versions
    return machines

#### We may want these to be something like: 
#### Restaurants, Hours?, Coupon Type? IDK
def machines_to_string(machines):
    s = ''
    for machine in machines:
        s += machine['name'] + ': ' + machine['time'] + '\n'
    return s

def room_names():
    s = 'Here are the laundry rooms that we have data for: \n'
    used = []
    for room in data.rooms:
        if data.rooms[room] not in used:
            s += room + '\n'
            used.append(data.rooms[room])
    return s

def makeSpecial():
    s = "Laundry Rooms: \n"
    s += '\n'.join([room for room in data.rooms])
    return s
    
############################
##       Top-Level        ##
############################

## return list of valid laundry rooms
special = makeSpecial()

def eval(cmd):
    return cmd['label']+'\n'+machines_to_string(getMachines(cmd['roomid'],cmd['machinetype']))
