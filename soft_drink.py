#from flask import Flask, render_template
import requests 
import json
from pprint import pprint
import numpy as np
import matplotlib.pyplot as plt
#from urllib.request import urlopen

#app = Flask(__name__)

yogurt_data = requests.get(
                      'https://world.openfoodfacts.org/api/v0/product/0894700010045.json')

yogurt_json = yogurt_data.json()

# data to plot
n_groups = 1
salt = (yogurt_json['product']['nutriments']['salt'],)
sodium = (yogurt_json['product']['nutriments']['sodium'],)
sugar = (int(yogurt_json['product']['nutriments']['sugars']),)

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
 
rects_salt = plt.bar(index, salt, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Salt')
 
rects_sodium = plt.bar(index + bar_width, sodium, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Sodium')

rects_sodium = plt.bar(index + 2*bar_width, sugar, bar_width,
                 alpha=opacity,
                 color='b',
                 label='Sugar')
                
plt.xlabel('Product')
plt.ylabel('Grams')
plt.title('Product Nutriments')
plt.xticks(index + bar_width, ('Yogurt',))
plt.legend()
plt.tight_layout()
plt.show()

'''
# Code for "Python Dictionaries"

# Get Json Data from the URL link
def get_json_data(url):
    return requests.get(url).json()

# List of soft drinks data
cola_data = get_json_data("https://world.openfoodfacts.org/api/v0/product/4890008100309.json")
dr_pepper_data = get_json_data("https://world.openfoodfacts.org/api/v0/product/8435185944009.json")
fanta_data = get_json_data("https://world.openfoodfacts.org/api/v0/product/8847100560094.json")
pepsi_data = get_json_data("https://world.openfoodfacts.org/api/v0/product/4060800100252.json")
sprite_data = get_json_data("https://world.openfoodfacts.org/api/v0/product/5449000014535.json")


array_of_data = [cola_data, sprite_data, fanta_data, dr_pepper_data,pepsi_data]
list_of_UPC_number = {}
for items in array_of_data:
   list_of_UPC_number[items['code']] = items['product']['product_name']  
pprint(list_of_UPC_number)



# add a data into a list
def add_data_into_list(list, data):
    list.append(data)

array_of_data = []
add_data_into_list(array_of_data, cola_data)
add_data_into_list(array_of_data, dr_pepper_data)
add_data_into_list(array_of_data, fanta_data)
add_data_into_list(array_of_data, pepsi_data)
add_data_into_list(array_of_data, sprite_data)



list_of_UPC_number = []
for item in array_of_data:
    add_data_into_list(list_of_UPC_number, item['code'])
print ("The list of UPC numbers are : ")
print (json.dumps(list_of_UPC_number) )  
print ('\n')


# add a key/value pair into a dictionary
def add_key_and_value_into_dic(dic, key, data):
    dic[key] = data


dic_of_UPC_and_soft_drinks = {}
for item in array_of_data:
    add_key_and_value_into_dic(dic_of_UPC_and_soft_drinks, item['code'], item['product']['product_name'])
print ("The dictionary of UPC numbers as keys and items' name as values are : ")
pprint(dic_of_UPC_and_soft_drinks)
print (json.dumps(dic_of_UPC_and_soft_drinks) )
print('\n')


dic_of_UPC_and_data = {}
for item in array_of_data:
    add_key_and_value_into_dic(dic_of_UPC_and_data, item['product']['product_name'], item['product']['nutriments'])
print ("The dictionary of items' name as keys and their data as values are : ")
pprint(dic_of_UPC_and_data)
print('\n')


# data to plot
n_groups = 5
salt = ()
sodium = ()
sugar = ()
for item in array_of_data:
    add_salt = (item['product']['nutriments']['salt'],)
    salt = salt + add_salt

    add_sodium = (item['product']['nutriments']['sodium'],)
    sodium = sodium + add_sodium

    add_sugar = (int(item['product']['nutriments']['sugars']),)
    sugar = sugar + add_sugar

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.25
opacity = 0.8
 
rects_salt = plt.bar(index, salt, bar_width,
                 alpha=opacity,
                 color='r',
                 label='Salt')
 
rects_sodium = plt.bar(index + bar_width, sodium, bar_width,
                 alpha=opacity,
                 color='g',
                 label='Sodium')

#rects_sodium = plt.bar(index + 2*bar_width, sugar, bar_width,
                # alpha=opacity,
                 #color='b',
                 #label='Sugar')
                
plt.xlabel('Product')
plt.ylabel('Grams')
plt.title('Product Nutriments')
plt.xticks(index + bar_width, ('Coke', 'Dr. Pepper', 'Fanta', 'Pepsi', 'Sprite'))
plt.legend()
plt.tight_layout()
plt.show()
'''


#if __name__ == "__main__":
 #   app.run(debug=True)
