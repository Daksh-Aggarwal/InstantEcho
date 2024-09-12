import time # for time functions
import pyperclip as pc # for clipboard access
import pyautogui # for interactions and alerts
import pyttsx3 as tts # for TTS

# Function to show a message using pyautogui alert
def show_alert(message):
    pyautogui.alert(message, "Message Details")

# Function to take a random message as input from the user
def random_message():
    # Input prompt
    message = pyautogui.prompt("Please enter your message:")
    if message:
        pc.copy(message)
        sent_time = time.ctime(time.time())
        time.sleep(3) # delay to simulate real message interaction
        receive_time = time.ctime(time.time())
        
        # Display the message and sent/receive time using alert
        message_details = (f"Message: \"{message}\".\n"
                           f"Sent at: {sent_time}.\n"
                           f"Message received at: {receive_time}.")
        # Instant voice output
        voice_output_message(message)

        # Alert to show the required details
        show_alert(message_details)

# Voice output function
def voice_output_message(message):
    engine = tts.init()
    engine.say("The message is " + message)
    engine.runAndWait()

# Running the program
def main():
    random_message()

if __name__ == "__main__":
    main()