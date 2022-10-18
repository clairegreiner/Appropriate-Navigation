import urllib.parse
import requests
import PySimpleGUI as sg

#you may need to run the command "python3 -m pip install PySimpleGUI" in order tro run this program





""" how to Create GUI's
1. copy this template and add/remove as needed
def guiname():
    layout = [  [sg.Text('this line will allow users to input values'), sg.InputText()],
                [sg.Text('some text')],
                [sg.Text('some text')],
                [sg.Button('button name'), sg.Button('button name')]]
    return sg.Window('name your window', layout)

2. create your window using the following code

window = guiname()

this will open the window you created in the def block
the whole layout is modular you can add some of the text lines or make more button lines, if you get stuck feel free to ask for help or google it.
other useful code:

window.close()                 <- this closes the current window
event, values = window.read()  <- allows your buttons to work as well as store input from users
varName = values[0]            <- this will store the user's input from the first sg.InputText() box incriment the 0 for more than one box eg(values[1] will be used for the second sg.InputText() box)
if event == 'button name':     <- this lets the program respond to button press
sg.theme('DarkBrown4')         <- changes the color of the GUI

sg.theme_previewer()           <-throw this code into the program to get a window displaying all the themes
"""


sg.theme('DarkBrown4')
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
    #creates GUI
    window = Home()
    #detects user interaction
    event, values = window.read()
    #closes program
    if event == 'Close' or event == sg.WIN_CLOSED:
        break
    #begins navigation page
    if event == "Navigate":
        window.close()
        window = nav()
        true = True
        while true == True:
            
            event, values = window.read()
            #closes window
            if event == 'Back' or event == sg.WIN_CLOSED:
                window.close()
                true = False
            #does Mapquest_parse-json_7's fuction
            if event == 'Route':
                route = True
                start = values[0]
                dest = values[1]
                main_api = "https://www.mapquestapi.com/directions/v2/route?"
                key = "efB9HJE5qFfoI6xGr5xqkDmnDAb0oCOe"
                
                while route == True:
                    url = main_api + urllib.parse.urlencode({"key":key, "from":start, "to":dest})

                    
                    json_data = requests.get(url).json()
                    #ends loop
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