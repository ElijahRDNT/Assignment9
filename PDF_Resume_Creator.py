import json

#read the json file
def read_data():
    jsonfile = open('C:/Users/lenovo/PLD Assignments/Assignment9/my_json.json', 'r')
    jsondata = jsonfile.read()

    obj = json.loads(jsondata)
    return obj



obj = read_data()

print(str(obj["full_name"]))