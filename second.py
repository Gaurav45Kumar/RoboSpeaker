import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")

    # Initialize the text-to-speech engine
    command = pyttsx3.init()

    # Set properties for the engine
    command.setProperty('rate', 150)  # Adjust the speech rate as needed

    while True:
        text = input("Enter what you want me to speak (or 'q' to quit): ")
        if text.lower() == "q":
            command.say("Goodbye, friend")
            command.runAndWait()
            break

        
        command.say(text)
        command.runAndWait()
