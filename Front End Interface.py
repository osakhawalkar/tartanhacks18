# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
#from webscrape import *
#from KNNHousing import *
#from zillow import *
from SplashScreen import *
#from Profile import *
####################################
# customize these functions
####################################

def init(data):
    # load data.xyz as appropriate
    data.hello = (data.width/2, data.height/5)
    data.new = (data.width/2, data.height/2)
    data.returning = (data.width/2, 4*data.height/5)#coordinates of buttons

    #screen states
    data.loggedIn = False #not logged in at the beginning
    data.startScreen = True
    data.createProfile = False
    data.logInScreen = False
    data.testProfile = False

    #profile data
    data.profile = None
    data.name = ""
    data.password = ""
    data.assets = ""
    data.risk = ""
    data.frequency = ""
    #entry fields booleans
    data.usernameField = False
    data.passwordField = False
    data.assetField = False
    data.riskField = False
    data.frequencyField = False
def mousePressed(event, data):
    # use event.x and event.y
    (newX, newY) = data.new
    (returningX, returningY) = data.returning
    while(data.startScreen):
        print(event.x, event.y)
        if(event.x > newX - 80 and event.x < newX + 80  and
            event.y > newY - 20 and event.y < newY + 20):
            data.startScreen = False
            data.createProfile = True
            print("Net Present Value Calculator")
        if (event.x > returningX - 50 and event.x < returningX + 50 and
            event.y > returningY - 20 and event.y < returningY + 20):
            data.startScreen = False
            data.logInScreen = True
            print("Recommender")
        if (returningX - 50 < event.x <  returningX + 50 and  returningY +40 < event.y <  returningY +80):
            data.startScreen = False
            data.testProfile = True
    if(data.logInScreen):
        # print(event.x, event.y)
        # print(newX - 75 < event.x < newX + 75 )
        # print(newY - 20 <event.y < newY + 20)
        if( (newX - 75 < event.x < newX + 75 ) and  (newY - 20 <event.y < newY + 20)):
            data.usernameField = not data.usernameField

        if( (returningX - 75 < event.x < returningX + 75) and (returningY - 20 < event.y < returningY + 20)):
            data.passwordField = not data.passwordField
    if (data.createProfile):
        if ((newX - 75 < event.x < newX + 75) and (newY - 20 < event.y < newY + 20)):
            data.usernameField = not data.usernameField
        if ((newX - 75 < event.x < newX + 75) and (newY + 20 < event.y < newY + 60)):
            data.passwordField = not data.passwordField
        if ((newX - 75 < event.x < newX + 75) and (newY +60 < event.y < newY + 100)):
            data.assetField = not data.assetField
        if ((newX - 75 < event.x < newX + 75) and (newY + 100 < event.y < newY + 140)):
            data.riskField = not data.riskField
        if ((newX - 75 < event.x < newX + 75) and (newY + 140 < event.y < newY + 180)):
            data.frequencyField = not data.frequencyField


def keyPressed(event, data):
    # use event.char and event.keysym
    if (data.usernameField):
        print("username")
        data.passwordField = False #disable entry into password field
        data.assetField = False
        data.riskField = False
        data.frequencyField = False

        if (event.keysym == "Enter"):
            data.usernameField = False
        if (event.keysym == "BackSpace"):
            data.name = data.name[:-1]
        if (event.char.isdigit()):
            data.name +=  event.char





    if (data.assetField):
        print("asset")
        data.usernameField = False
        data.passwordField = False
        data.riskField = False
        data.frequencyField = False
        # disable entry into password field
        if (event.keysym == "Enter"):
            data.assetField = False
        if (event.keysym == "BackSpace"):
            data.assets = data.assets[:-1]
        if (event.char.isdigit()):
            data.assets += event.char

    if (data.riskField):
        print("risk")
        data.usernameField = False
        data.passwordField = False
        data.assetField = False
        data.frequencyField = False
        # disable entry into password field
        if (event.keysym == "Enter"):
            data.riskField = False
        if (event.keysym == "BackSpace"):
            data.risk = data.risk[:-1]
        if (event.char.isdigit()):
            data.risk += event.char

    if (data.frequencyField):
        print("frequency")
        data.usernameField = False
        data.passwordField = False
        data.assetField = False
        data.riskField = False
        # disable entry into password field
        if (event.keysym == "Enter"):
            data.frequency = False
        if (event.keysym == "BackSpace"):
            data.frequency = data.frequency[:-1]
        if (event.char.isdigit()):
            data.frequency += event.char
def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw in canvas
    if(data.startScreen):
        startScreen(canvas, data)

    if(data.logInScreen):
        RECsystem(canvas, data)

    if(data.createProfile):
        NPV(canvas,data)



####################################
# use the run function as-is
####################################

def run(width=1000, height=500):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000, 500)