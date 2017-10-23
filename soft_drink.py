import requests 
import json
from pprint import pprint

# Get Json Data from the URL link
def get_json_data(url):
    return requests.get(url).json()


pepsi_data = get_json_data("https://world.openfoodfacts.org/api/v0/product/4060800100252.json")
sprite_data = get_json_data("https://world.openfoodfacts.org/api/v0/product/5449000014535.json")
fanta_data = get_json_data("https://world.openfoodfacts.org/api/v0/product/8847100560094.json")
dr_pepper_data = get_json_data("https://world.openfoodfacts.org/api/v0/product/8435185944009.json")
coke_data = get_json_data("https://world.openfoodfacts.org/api/v0/product/4890008100309.json")


# add a data into a list
def add_data_into_list(list, data):
    list.append(data)

list_of_data = []
add_data_into_list(list_of_data, pepsi_data)
add_data_into_list(list_of_data, sprite_data)
add_data_into_list(list_of_data, fanta_data)
add_data_into_list(list_of_data, dr_pepper_data)
add_data_into_list(list_of_data, coke_data)


list_of_UPC_number = []
for item in list_of_data:
    add_data_into_list(list_of_UPC_number, item[u'code'])
print "The list of UPC numbers are : "
print json.dumps(list_of_UPC_number)    #prints without 'u' character showing at the front
print ('\n')


# add a key/value pair into a dictionary
def add_key_and_value_into_dic(dic, key, data):
    dic[key] = data

dic_of_UPC_and_soft_drinks = {}
for item in list_of_data:
    add_key_and_value_into_dic(dic_of_UPC_and_soft_drinks, item[u'code'], item[u'product'][u'product_name'])
print "The dictionary of UPC numbers as keys and items' name as values are : "
pprint(dic_of_UPC_and_soft_drinks)
print('\n')


dic_of_UPC_and_data = {}
for item in list_of_data:
    add_key_and_value_into_dic(dic_of_UPC_and_data, item[u'product'][u'product_name'], item[u'product'][u'nutriments'])
print "The dictionary of items' name as keys and their data as values are : "
pprint(dic_of_UPC_and_data)
print('\n')


