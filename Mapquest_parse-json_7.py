import urllib.parse
import requests

#Definitions
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "efB9HJE5qFfoI6xGr5xqkDmnDAb0oCOe"
#main loop
while True:
    #input values
    Start = input("Please enter where you're coming from" + "\n")
    Destination = input("please enter where you are heading" + "\n")
    
    #url parse
    url = main_api + urllib.parse.urlencode({"key":key, "from":Start, "to":Destination})

    #retrieve url
    json_data = requests.get(url).json()
    
    #print url and info sorting
    print("URL: " + (url)) 
    json_data = requests.get(url).json() 
    json_status = json_data["info"]["statuscode"] 
    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n") 
        #displays travel stats
        print("=============================================") 
        print("Directions from " + (Start) + " to " + (Destination)) 
        print("Trip Duration:   " + (json_data["route"]["formattedTime"])) 
        print("Miles: " + str("{:.2f}".format(json_data["route"]["distance"]))) 
        print("Fuel Used (Gal): " + str("{:.2f}".format(json_data["route"]["fuelUsed"]))) 
        print("Kilometers:  " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        #displays directions
        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)")) 
        print("=============================================\n") 
    #shows if one or more inputs is invalid
    elif json_status == 402: 
        print("**********************************************") 
        print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.") 
        print("**********************************************\n") 
    #shows if one or more entries is missing
    elif json_status == 611: 
        print("**********************************************") 
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.") 
        print("**********************************************\n") 
    #catchall
    else: 
        print("************************************************************************") 
        print("For Staus Code: " + str(json_status) + "; Refer to:") 
        print("https://developer.mapquest.com/documentation/directions-api/status-codes") 
        print("************************************************************************\n")

    #exit condition
    Continue = input("would you like to exit? Y/N \n")
    if Continue == "Y" or Continue == "y" or Continue == "Yes" or Continue == "yes" or Continue == "YES":
        break
