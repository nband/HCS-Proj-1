## box is a list of commands
## a command is a dictionary containing a list of tags that uniquely identify it
## along with all the information needed to run the command
#### I'm fairly certain there's a way to generate this systematically instead of manually inputting...I hope
"""
I also removed everything except for what was there for the first service, 'L' (I removed a fair chunk
of 'L' in order to make this file a little less enormous for ease of reading purposes)
You are welcome to check the previous version of this file to see what was previously there
"""
box = [
    {'service': 'L', 'args':{ 'roomid':'1362520', 'machinetype':'washer', 'label': 'DUNSTER HOUSE K Washers'}, 'tags': ['DUNSTER', 'HOUSE', 'K', 'LAUNDRY', 'WASHERS', 'WASHER']},
    {'service': 'L', 'args':{ 'roomid':'1362520', 'machinetype':'dryer', 'label': 'DUNSTER HOUSE K Dryers'}, 'tags': ['DUNSTER', 'HOUSE', 'K', 'LAUNDRY', 'DRYER', 'DRYERS']},
    {'service': 'L', 'args':{ 'roomid':'1362521', 'machinetype':'washer', 'label': 'DUNSTER HOUSE G Washers'}, 'tags': ['DUNSTER', 'HOUSE', 'G', 'LAUNDRY', 'WASHERS', 'WASHER']},
    {'service': 'L', 'args':{ 'roomid':'1362521', 'machinetype':'dryer', 'label': 'DUNSTER HOUSE G Dryers'}, 'tags': ['DUNSTER', 'HOUSE', 'G', 'LAUNDRY', 'DRYER', 'DRYERS']},
    {'service': 'L', 'args':{ 'roomid':'1362556', 'machinetype':'dryer', 'label': 'MATHER HOUSE LOW RISE Dryers'}, 'tags': ['MATHER', 'HOUSE', 'LOW', 'RISE', 'LAUNDRY', 'DRYER', 'DRYERS']},
]
