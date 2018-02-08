
# Python JSON encoders and decoders 
# JSON        Python
# obj         dict
# arr         list
# string      str 
# int         int
# float       float
# true        True
# false       false
# none        None 

import json

people_string = '''
{
    "people": [
        {
            "name": "vivek mathapati",
            "phone": "9980923664",
            "email": ["vivekanand.d.mathapati@gmail.com", "vivek@gmail.com"],
            "has_license": false
        },
        {
            "name": "veer munnolimath",
            "phone": "678678687",
            "email": ["veer.d.mathapati@gmail.com", "veer@gmail.com"],
            "has_license": true
        }
    ]
}
'''

data = json.loads(people_string)
# print(type(data))
# print(type(data['people']))
for people in data['people']:
    del people['phone']

new_string =  json.dumps(data,indent = 2,sort_keys = True)
# print(new_string)


#load json file 

with open('states.json') as f:
    data = json.load(f)
    for state in data['states']:
        del state['area_codes']

with open('new_states.json','w') as wf:
    new_string = json.dump(data, wf, indent = 2, sort_keys = True)
