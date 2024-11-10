from app import tts

def say(message):
    tts("rushia", 20, message, "en-US-AnaNeural-Female", 8, "pm", 1, 0.33)

if __name__ == "__main__":
    say("hello my name is rushia, i love rushia rushia rushia")