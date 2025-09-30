
fav_nums = {'bob': 3,
            'rob': 6,
            'sarah': 9,
            'tim': 0,
            'grog': 8,
            }

for name, num in fav_nums.items():
    print(f"{name.title()}'s favorite number is {num}.")
print("")
print("----------------------------------------------------------------------------------------------------------------------------------------\n")

py_glossary = {'list': 'collection of values stored in square brackets[].',
               'variable': 'like a folder which holds informations.',
               'for loop': 'used to iterate through lists, tuples, dictionaries and so on.',
               'boolean value': 'simple value of True and False when given conditions are met.',
               'string': 'line of text surround by quotation markers or apostrophes.',
               }

for word, definition in py_glossary.items():
    print(f"{word.title()}\n {definition.capitalize()}\n")

print("----------------------------------------------------------------------------------------------------------------------------------------\n")

major_rivers = {'nile': 'egypt',
            'amazon river': 'brazil',
            'the ganges': 'india',
            }

for river, country in major_rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("")
for country in major_rivers.values():
    print(country.title())
print("")

print("----------------------------------------------------------------------------------------------------------------------------------------\n")
favorite_languages = {'jen': 'python',
                      'sarah': 'c',
                      'edward': 'rust',
                      'phil': 'python',
                      }

fav_language_list = ['jen', 'sarah', 'edward', 'phil', 'john', 'cams', 'tom', 'kyle', 'mads']

for name in fav_language_list:
    if name in favorite_languages:
        print(f"Thank you {name} for taking the poll.")
    else:
        print(f"Please, take the poll {name}.")
print("")
print("----------------------------------------------------------------------------------------------------------------------------------------\n")


person_1= {'first name': 'bob', 
           'last name': 'proctor',
           'city': 'new york',
           }

person_2 = {'first name': 'hector',
            'second name': 'zeroni',
            'city': 'brookelyn',
            }

person_3 = {'first name': 'stanley',
            'second name': 'yelnats',
            'city': 'brookelyn',
            }

people = [person_1, person_2, person_3]

for persons in people:
    for key, value in persons.items():
        print(f"{key.title()}: {value.title()}")
    print("")
print("----------------------------------------------------------------------------------------------------------------------------------------\n")

pet_1 = {'alligator': 'steve',}
pet_2 = {'gold fish': 'harvey',}         
pet_3 = {'dog': 'rebecca'}
pet_4 = {'cat': 'robbie'}
pet_5 = {'parrot': 'luna'}
pet_6 = {'rat': 'robert'}

pets = [pet_1, pet_2, pet_3, pet_4, pet_5, pet_6]

for pet in pets:
    for key, value in pet.items():
        print(f"The {key} belongs to {value.title()}.")
print("")
print("----------------------------------------------------------------------------------------------------------------------------------------\n")

favorite_places = {'tobey': ['home', 'egypt', 'ghana'],
                   'ronk': ['paris', 'nepal'],
                   'rockie': ['portugal', 'spain', 'somalia'],
                   }

for key, value_list in favorite_places.items():
    print(f'{key.capitalize()}')
    for item in value_list:
        print(f" . {item}")
    print("")
print("----------------------------------------------------------------------------------------------------------------------------------------\n")

av_nums = {'bob': [3,6,7,2],
            'rob': [2,8],
            'sarah': [8,],
            'tim': [0,1,6],
            'grog': [3,0,9],
            }

for name, num_list in av_nums.items():
    print(f"{name.capitalize()}'s favorite numbers are --> {num_list}")
print("")
print("----------------------------------------------------------------------------------------------------------------------------------------\n")

cities = {
    'barcelona': {
        'country': 'spain',
        'population': '1.6 million',
        'fact': 'it is the capital city of Spain.',
        },

    'new delhi': {
        'country': 'india',
        'population': '33.8 million',
        'fact': 'it is the capital city of India.'
        },

    'london': {
        'country': 'united kingdom',
        'population': '9 million',
        'fact': 'it is the capital city of the UK.'
        }

    }

for city, info in cities.items():
    information = f"is in the country of {info['country'].capitalize()}. It has a population of {info['population']} and {info['fact']}"
    print(f"{city.title()} {information}\n")

print("----------------------------------------------------------------------------------------------------------------------------------------\n")




    
        

        

    