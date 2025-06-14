import time # for time functions
import pyperclip as pc # for clipboard access
import pyautogui # for interactions and alerts
import pyttsx3 as tts # for TTS

# Function to take a random message as input from the user
def random_message():
    message = input("Please enter the message: ")
    pc.copy(message)
    sent_time = time.ctime(time.time())
    print(f"\nThe Copied Whatsapp message is \"{message}\".\n")
    return message, sent_time

# Function to display the message along with the time at which the message was sent and received
def show_message(message, sent_time):
    print("Receiving the message...")
    time.sleep(3) # delay to simulate real message interaction
    receive_time = time.ctime(time.time())
    print(f"Message received. Here's the message: \"{message}\".\n"
          f"Message sent at {sent_time}.\n"
          f"Message received at {receive_time}.")
    voice_output_message(message)

# Voice output function
def voice_output_message(message):
    engine = tts.init()
    engine.say("The message is " + message)
    engine.runAndWait()

# Function to running the program
def main():
    message, sent_time = random_message()
    show_message(message, sent_time)

if __name__ == "__main__":
    main()
