import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
map_api = "https://www.mapquestapi.com/staticmap/v5/map?"
key = "HjtEWcDVwNgGTsz4OeAuL8cC0g2wQqwh"



while True:
    orig = input("Starting Location: ")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destination: ")
    if dest == "quit" or dest == "q":
        break
    url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})
    #map_url = map_api + urllib.parse.urlencode({"key":key, "start":orig, "end":dest, "size":size, "type":Type, "traffic":traffic})
    #map_url is a place holder for testing reasons, can be removed at a later time 20221019 1128am
    print("URL: " + (url))
    #print("Map: " + (map_url));place holder for testing reasons, can be removed at a later time 20221019 1128am
    json_data = requests.get(url).json()
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]


    size = "@2x" #map size
    Type = "hyb" #this will determine the type of map displayed; map, hyb, sat, light, darkwhile True:
    size = "@2x"
    Type = "hyb"
    traffic = "flow|con|inc"
    map_url = map_api + urllib.parse.urlencode({"key":key, "start":orig, "end":dest, "size":size, "type":Type, "traffic":traffic})
        #map url format can be adjusted to display other values, orig and dest pulled from ln 11&14
    print("Map: " + (map_url))
    #this while true is used to set the parameters and display the map

    if json_status == 0:
      print("API Staus: " + str(json_status) + " = A successful route call.\n")
      print("============================================")
      print("Directions from " + (orig) + " to " +(dest))
      print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
      print("Miles:           " + str("{:.2f}".format(json_data["route"]["distance"])))
      print("Fuel Used (Gal): " + str("{:.2f}".format(json_data["route"]["fuelUsed"])))
      print("============================================")
      for each in json_data["route"]["legs"][0]["maneuvers"]:
          print((each["narrative"]) + " (" + str("{:.2f}".format ((each["distance"])) + " mi)"))
      print("============================================\n")
    elif json_status == 402:
        print("********************************************")
        print("Status Code: " + str(json_status) + "; Invalid User inputs for one or both locations.")
        print("********************************************\n") 
    elif json_status == 611:
        print("********************************************")
        print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
        print("********************************************\n") 
    else:
        print("**************************************************************************") 
        print("For status code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("**************************************************************************\n")




