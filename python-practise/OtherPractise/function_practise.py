#function practise/ Exercise 141 in Python Crash Course Book
""" def city_country(city, country):

    cityncountry = f"{city.title(), {country.title()}}"
    return cityncountry

print(city_country("santiago", "chile"))
print(city_country("new delhi", "india"))
print(city_country("tokyo", "japan"))

def make_album(artist_name, album, song_num = None):

    album1 = {"artist": artist_name.title(), "song": album.title()}
    album2 = {"artist": artist_name.title(), "song": album.title()}
    album3 = {"artist": artist_name.title(), "song": album.title()}
    user_album = {"artist": artist_name.title(), "song": album.title()}

    while True:
        print("\nHere you can choose your own artist and their album.")
        user_artist = input("Type the name of the artist here: ")
        user_album = input("Type the artist's album here: ")

        print("Would you like to quit.")   
        user_ans = input("yes or no: ")

        if user_ans == 'yes':
            break    

        user_album = make_album(user_artist, user_album)
        print(user_album)

    #if song_num:
        #album1["song_number"] = song_num
        #album2["song_number"] = song_num
       # album3["song_number"] = song_num 

    
    

album1 = make_album("nf", "hope", 2)
album2 = make_album("ye", "i wonder", 4)
album3 = make_album("eminem", "godzilla", 6)

        
""" """ 
print(album1)
print(album2)
print(album3) """ 


#function, passing arbitary number of arguements practice

def sandwhich_toppings(*topping):
    print("")
    print("Sandwich with:")
    for toppings in topping:
        print(toppings)
    print("Is being prepared.") 
        
sandwhich_toppings("tomatoes", "cucumbers", "ketchup")
sandwhich_toppings("mayo", "tomatoes", "potatoes", "cheese", "onions")

print("---------------------------------------------------------------------------------------------------------------")


def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('Madhvan', 'Devji', location='unknown', favorite_sports='football')

print(user_profile)


print("---------------------------------------------------------------------------------------------------------------")


def car_information(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model name'] = model_name
    return car_info
    


car_details = car_information('subaru', 'outback', color='blue', tow_package=True)
print(car_details)