class Button:
    def __init__(self):
        self.button = None
        self.build = None
        self.hold = False

    def createButton(self):
        self.button = loadImage("play-button.png", "png")
        self.build = loadImage("repair.png")

    def display(self):
        image(self.button, 100-32, 510)
        image(self.build, 400, 510)

    def isPressed(self):
        if mouseX > 68 and mouseX < 132:
            if mouseY > 510 and mouseY < 542:
                if (mousePressed  and mouseButton == RIGHT) or self.hold == True:
                    self.hold = True
                    return True
        else:
            if self.hold:
                return True
        return False

    def isBuiltPressed(self):
        if mouseX > 400 and mouseX < 432:
            if mouseY > 510 and mouseY < 542:
                if mousePressed and mouseButton == RIGHT:
                    print("Built complete")
                    print("Press RUN to visualize")
                    return True
        return False

