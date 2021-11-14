import json

# json string -  treat it as a string

#loads()
county_json_string = """
{  "name": "United States",
   "population": 331002651,
   "state of usa" : "true"
}"""
print (county_json_string[9])
print(type(county_json_string)) ## output confirms indeed a string

#loads will convert json string to python object dict (not always) or list depending upon the input
# array -> list
# json -> dict
# null -> None
# Boolen (true/false) -> True/False
# String -> str

py_country_dict = json.loads(county_json_string)
print (type(py_country_dict))
print(py_country_dict['name']+ " and " + py_country_dict['state of usa'])

#returing json_string to python object (list)
countries = '["United States", "Canada"]'
py_countries_list = json.loads(countries)
print(type(py_countries_list))
print(py_countries_list[1])

# load() - covners json file to python object
#requires python open() to open the file

with open ("C:\\SparkScala\\inputData\\usa.json") as usaFP:
    python_obj = json.load(usaFP)
## end of file

print(type(python_obj))
print(python_obj['languages'])
print(type(python_obj['languages']))

#===========================================================
# dumps() -  coverts a python object (list/tuple, str, dict, int/float) to json string(array, string, json, number)

languages = ("English", "French") #tuple
json_arr = json.dumps(languages)
print (json_arr)
print (type(json_arr))

country_dict = {
    "name": "Canada",
    "population": 37742154,
    "languages": languages,
    "president": None  ## will be converted to null (when converted to json string)
}
json_string = json.dumps(country_dict)
print (json_string)
print (type(json_string))

## dump() - converts python object (dict) to json_file
with open ("C:\\SparkScala\\inputData\\usa_new.json", 'w') as uf:
    json.dump(country_dict, uf, indent=4)

