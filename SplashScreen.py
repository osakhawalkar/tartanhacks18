from tkinter import *
def startScreen(canvas,data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='AntiqueWhite1', width=0)

    (helloX , helloY) = data.hello
    #canvas.create_rectangle(helloX - 60 , helloY - 20, helloX + 60, helloY + 20, width= 5, fill = "grey" )
    canvas.create_text(data.hello, text = "Welcome to Shillow")

    (newX, newY) = data.new
    canvas.create_rectangle(newX - 80, newY - 20 , newX + 80 , newY + 20, width = 5, fill = "grey")
    canvas.create_text(data.new, text = "Net Present Value Calculator")

    (returningX, returningY) = data.returning
    canvas.create_rectangle(returningX - 50, returningY - 20, returningX + 50, returningY +20, width = 5, fill = "grey")
    canvas.create_text(data.returning, text = "Recommender")



def RECsystem(canvas, data):
    canvas.create_rectangle(0, 0, data.width, data.height,
                            fill='AntiqueWhite1', width=0)

    (helloX, helloY) = data.hello
    # canvas.create_rectangle   (helloX - 60 , helloY - 20, helloX + 60, helloY + 20, width= 5, fill = "grey" )
    canvas.create_text(data.hello, text="Recommendation Mode", font = "120")

    (newX, newY) = data.new
    new = (newX - 80, newY)
    canvas.create_rectangle(newX - 75, newY - 20, newX + 75, newY + 20, width = 2 , fill="white")
    canvas.create_text(newX - 75, newY, text = data.name, anchor = 'w')
    canvas.create_text(new, text="Zip Code", anchor = 'e')

    (returningX, returningY) = data.returning
    returning = (returningX - 80, newY + 40)
    canvas.create_rectangle(returningX - 75, newY + 20, returningX + 75, newY + 60 , width= 2 , fill="white")
    canvas.create_text(returningX - 75, newY + 40, text = data.password, anchor = 'w')
    canvas.create_text(returning, text="Bedrooms", anchor ='e')

    returning = (returningX - 80, newY + 80 )
    canvas.create_rectangle(returningX - 75, newY + 60, returningX + 75, newY + 100, width= 2 , fill="white")
    canvas.create_text(returningX - 75, newY + 80, text = data.assets, anchor = 'w')
    canvas.create_text(returning, text="Bathrooms", anchor ='e')

    returning = (returningX - 80, newY + 120 )
    canvas.create_rectangle(returningX - 75, newY + 100, returningX + 75, newY + 140, width= 2 , fill="white")
    canvas.create_text(returningX - 75, newY + 120, text = data.risk, anchor = 'w')
    canvas.create_text(returning, text="Square Feet", anchor ='e')


    # Label(canvas, text="Username").grid(row=1, column=1, sticky=W)  # entry fields
    # Label(canvas, text="Password").grid(row=2, column=1, sticky=W)
    #
    # data.name = Entry(canvas, textvariable=data.name, justify=RIGHT).grid(row=1, column=2)  # entry field data with positioning
    #
    # data.password = Entry(canvas, textvariable=data.password, justify=RIGHT).grid(row=2, column=2)


    # btCalculate = Button(window, text="Calculate", command=self.Calculate).grid(row=6, column=2,
    #                                                                             sticky=E)  # calculate button


def NPV(canvas,data): #ask for name, assets, risk, frequency, password
    canvas.create_rectangle(0, 0, data.width, data.height,
                           fill='AntiqueWhite1', width=0)
    (helloX, helloY) = data.hello
    # canvas.create_rectangle(helloX - 60 , helloY - 20, helloX + 60, helloY + 20, width= 5, fill = "grey" )
    canvas.create_text(data.width/2,0, text="Net Present Value", font = "120", anchor = "n")

    (newX, newY) = data.new
    new = (newX - 80, newY)
    canvas.create_rectangle(newX - 75, newY - 20, newX + 75, newY + 20, width = 2 , fill="white")
    canvas.create_text(newX - 75, newY, text = data.name, anchor = 'w')
    canvas.create_text(new, text="Zipcode", anchor = 'e')

    (returningX, returningY) = data.returning

    returning = (returningX - 80, newY + 80 )
    canvas.create_rectangle(returningX - 75, newY + 60, returningX + 75, newY + 100, width= 2 , fill="white")
    canvas.create_text(returningX - 75, newY + 80, text = data.assets, anchor = 'w')
    canvas.create_text(returning, text="Years", anchor ='e')

    returning = (returningX - 80, newY + 120 )
    canvas.create_rectangle(returningX - 75, newY + 100, returningX + 75, newY + 140, width= 2 , fill="white")
    canvas.create_text(returningX - 75, newY + 120, text = data.risk, anchor = 'w')
    canvas.create_text(returning, text="Years In Place", anchor ='e')

    returning = (returningX - 80, newY + 160 )
    canvas.create_rectangle(returningX - 75, newY + 140, returningX + 75, newY + 180, width= 2 , fill="white")
    canvas.create_text(returningX - 75, newY + 160, text = data.frequency, anchor = 'w')
    canvas.create_text(returning, text="Yearly Income", anchor ='e')

