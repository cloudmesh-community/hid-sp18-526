from tinydb import TinyDB, Query

import constants

db = TinyDB(constants.DATA_DIRECTORY + '/db.json')

def search():
    return db.all()

def get(key):
    Q = Query()
    search = db.search(Q.key == key)
    if search:
        return search[0]['value']
    
def put(key, value):
    if get(key):
        Q = Query()
        return db.update({'value': value}, Q.key == key)
    else:
        return db.insert({'key': key, 'value': value})
    
def delete(key):
    Q = Query()
    return db.remove(Q.key == key)
    

