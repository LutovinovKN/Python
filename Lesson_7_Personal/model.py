import json


change_field = {'id' : id,
                'name' : name,
                'surname' : surname,
                'number' : number,
                'number+' : work_number
                }

list_id = []

with open("contact.json", "w") as write_file:
    json.dump(data, write_file)
    
    import datetime

class Contact:
    def __init__ (self, name, surname, number, position = None, date_created = None, date_updated = None):
        self.name = name
        self.surname = surname
        self.number = number
        self.position = position
        self.date_created = date_created if date_created is not None else datetime.datetime.now().isoformat()
        self.date_updated = date_updated if date_updated is not None else datetime.datetime.now().isoformat()

    def __repr__ (self) -> str:
        return f"({self.name}, {self.surname}, {self.number}, {self.position}, {self.date_created}, {self.date_updated})"



