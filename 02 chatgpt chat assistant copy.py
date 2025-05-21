import openai

try:
    import speech_recognition as sr
except ImportError:
    sr = None

openai.api_key = "####"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

use_voice = False
if sr is not None:
    choice = input("Would you like to use voice input? (y/n)\n").lower()
    use_voice = choice.startswith("y")
    if use_voice:
        recognizer = sr.Recognizer()
        mic = sr.Microphone()

def get_user_input():
    if use_voice:
        with mic as source:
            print("Listening...")
            audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I did not understand. Please type your message.")
            return input()
        except sr.RequestError:
            print("Speech recognition service is unavailable. Falling back to text.")
            return input()
    else:
        return input()

print("Your new assistant is ready! (type quit() to exit)")
while True:
    message = get_user_input()
    if message.strip() == "quit()":
        break
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")
