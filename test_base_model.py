#!/usr/bin/python3

from models.base_model import BaseModel

my_model = BaseModel()
my_model.name = "Holberton"
my_model.my_number = 89
print(my_model)
""" [BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89,
'name': 'Holberton',
'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434),
'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)} """
my_model.save()
print(my_model)
"""[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89,
'name': 'Holberton',
'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119572),
'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119427)}"""
my_model_json = my_model.to_dict()
print(my_model_json)
"""{'my_number': 89,
'name': 'Holberton',
'__class__': 'BaseModel',
'updated_at': '2017-09-28T21:05:54.119572',
'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579',
'created_at': '2017-09-28T21:05:54.119427'}"""
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]),
                                   my_model_json[key]))
    """ my_number: (<class 'int'>) - 89
    name: (<class 'str'>) - Holberton
    __class__: (<class 'str'>) - BaseModel
    updated_at: (<class 'str'>) - 2017-09-28T21:05:54.119572
    id: (<class 'str'>) - b6a6e15c-c67d-4312-9a75-9d084935e579
    created_at: (<class 'str'>) - 2017-09-28T21:05:54.119427"""
