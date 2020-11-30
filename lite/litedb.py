import json
import os


class LiteDB(object):
    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load(self.location)
    
    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        
        return True
    
    def _load(self):
        self.db = json.load(open(self.location, "r"))
    
    def dump(self):
        try:
            json.dump(self.db, open(self.location, "w+"))
            return True
        except:
            return False
    
    def set(self, key, value):
        try:
            self.db[str(key)] = value
            self.dump()
            return True
        except Exception as e:
            print("[X} Error Saving Values To Database: " + str(e))
            return False
    
    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            print(f"No Value Can Be Found For {str(key)}")
    
    def delete(self, key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dump()
        return True
    
    def reset(self):
        self.db={}
        self.dump()
        return True

