import urllib.parse
import requests
import PySimpleGUI as sg



sg.theme('DarkBrown4')   # Add a touch of color
#home GUI
def Home():
    layout = [  [sg.Text('Welcome to Appropriate navigation')],
                [sg.Text("")],
                [sg.Text('     What would you like to do?')],
                [sg.Button('Navigate'), sg.Text("                     "), sg.Button('Close')]]
    return sg.Window('Appropriate Navigation', layout)

#Navigation GUI
def nav():
    layout = [  [sg.Text('                           Welcome to navigation')],
            #[sg.Button("", key='-TEXT-', enable_events= True)],  
            [sg.Text("")],
            [sg.Text('Where are you coming from?'), sg.InputText()],
            [sg.Text('Where are you going?          '), sg.InputText()],
            [sg.Button('Route'), sg.Text("    "), sg.Button('Back')]]
    return sg.Window('Appropriate Navigation', layout)





#main GUI program
while True:
    window = Home()
    event, values = window.read()
    if event == 'Close' or event == sg.WIN_CLOSED:
        break
    if event == "Navigate":
        window.close()
        window = nav()
        true = True
        while true == True:
            event, values = window.read()
            
            if event == 'Back' or event == sg.WIN_CLOSED:
                window.close()
                true = False
            if event == 'Route':
                route = True
                start = values[0]
                dest = values[1]
                main_api = "https://www.mapquestapi.com/directions/v2/route?"
                key = "efB9HJE5qFfoI6xGr5xqkDmnDAb0oCOe"
                #main loop
                while route == True:
                    url = main_api + urllib.parse.urlencode({"key":key, "from":start, "to":dest})

                    #retrieve url
                    json_data = requests.get(url).json()
                    route = False
#ive made it up to the point of implimenting the original program, none of the data is parsed but the URL integer works like normal so programming should work as if you were in the original file.            
                    
    
      






#this is just the main block from the original lab, i've implimented it into my UI but leave it here for reference
#main_api = "https://www.mapquestapi.com/directions/v2/route?"
#key = "efB9HJE5qFfoI6xGr5xqkDmnDAb0oCOe"
#main loop
#while True:
#    url = main_api + urllib.parse.urlencode({"key":key, "from":start, "to":dest})
#
    #retrieve url
#    json_data = requests.get(url).json()
    
    #print url and info sorting
#    print("URL: " + (url))