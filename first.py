import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    text = input("Enter what you want me to speak: ")

    # Initialize the text-to-speech engine
    command = pyttsx3.init()

   
    command.say(text)
    command.runAndWait()
