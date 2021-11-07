import json

# json string -  treat it as a string
county_json_string = """
{  "name": "United States",
   "population": 331002651
}"""
print (county_json_string[9])
print(type(county_json_string))

#loads will convert json string to python object dict (not always) or list depending upon the input
py_country_dict = json.loads(county_json_string)
print (type(py_country_dict))
print(py_country_dict['name'])

#returing string to python object (list)
countries = '["United States", "Canada"]'
py_countries_list = json.loads(countries)
print(type(py_countries_list))
print(py_countries_list[1])

