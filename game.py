import time

rooms = {
    "living_room": {
        "description": "You are in the living room, there is a large TV and a big couch.",
        "exits": {"north": "kitchen", "east": "bedroom"}
    },
    "kitchen":{
        "description": "",
        "exits":{"south":"hall"}
    },
    "hall":{
        "description":"",
        "exits":{"west":"door"}
    }
    } 
