import speech_recognition as sr
import webbrowser as wb
import pywhatkit as kit
import pyttsx3 as ptx
def voice():
    r=sr.Recognizer()
    with sr.Microphone() as source:
            print("david is here..How can I help you my boss.....")
            frnd=ptx.init()
            frnd.say('david is here.how can i help you..my boss..?')
            frnd.runAndWait()
            r.pause_threshold=0.6
            audio= r.listen(source)
    try:
        ask=r.recognize_google(audio, language='en-us')
        print(f'yes sure my boss.I will do that for you...just enjoy my service')
        frnd=ptx.init()
        frnd.say('yes sure my boss.I will do that for you...just enjoy my service')
        frnd.runAndWait()
        kit.playonyt(ask)
 
    except:
        print('I can not hear you properly...')
        frnd=ptx.init()
        frnd.say('sorry boss...I can not hear your order properly..will you kindly say that again..please..')
        frnd.runAndWait()
        voice()
        return ''
        return ask

voice()



