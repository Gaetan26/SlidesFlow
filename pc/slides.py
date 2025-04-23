import keyboard 

def nextSlide():
    keyboard.press_and_release("right")
    return True

def previousSlide():
    keyboard.press_and_release("left")
    return True