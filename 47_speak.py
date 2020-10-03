def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVOice")
    speak.Speak("Hi.. kinjal. take care of you")        #using this speak.

if __name__ == '__main__':
    speak("You are the best")