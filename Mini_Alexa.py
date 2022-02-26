import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import sys
import webbrowser
from datetime import date



engine=pyttsx3.init()
engine.setProperty("rate",150)
voices=engine.getProperty("voices")
engine.setProperty('voice',voices[1].id)
recognizer=sr.recognizer()


def engine_talk(text):
  engine.say(text)
  engine.runandWait()

def run_alexa():
  with sr.Microphone() as source:
    recognizer.adjust_for_ambient_noise(source,duration=1)
    print('\n')
    print("Start Speaking!!")
    engine_talk('listening...')
    recordedaudio=recognizer.listen(source)
  try:
    command=recognizer.recognize_google(recordedaudio,language='en-in')
    command=command.lower()
    if 'alexa' in command:
      command=command.replace('alexa','')
      print('you said'+commmand)
    else:
      print('you said :'+command)
    
    if 'hello' in command:
      print('hello how can I help you ?')
      engine_talk('hello, how can I help you?')
    
    elif 'who are you' in command:
      print('I am mini alexa aka your virtual assistant master')
      engine_talk('I am mini alexa aka your virtal assistant master. how can i help you?')
    
    elif 'can you do' in command:
      print('''I can play songs on youtube, tell ypu are a joke, search on wikipedia, tell date and time, find your location, locate area on map, open different websites websites like instagram, youtube,gmail,git hub,stack overflow and seaches on google. How may I help you??''')
      engine_talk('''I can play songs on youtube, tell you a joke, search on wikipedia, tell date and time,find your location,locate area on map, open different websites like instagram,youtube, gmail,git hub,stack overflow and searches on google. How may I help ypu??''')

    elif 'play' in command:
      song=command.replace('paly','')
      print('playing'+song)
      engine_talk('playing'+song)
      pywhatkit.playonyt(song)

    elif 'date and time' in command:
      today=date.today()
      time=datetime.datetime.now().strftime('%I:%M %p')
      d2=today.strftime('%B %d %Y')
      print("Today's Date is",d2,'Current Time is', time)
      engine_talk('Today is :'+d2)
      engine_talk('and current time is'+time)
    
    elif 'time and date' in command:
      today=date.today()
      time=datetime.datetie.now().strftime('%I: %M %p')
      d2=today.strftime("%B %d %Y")
      print("Today's Date is",d2,'Current time is',time)
      engine_talk('Current time is'+time)
      engine_talk('and Today is:'+d2)

    elif 'time' in command:
      time=datetime.datetime.now().strftime("%I: %M %p")
      print('The Current time is'+time)
      engine_talk('The Current time is ')
      engine_talk(time)
    
    elif 'date' in command:
      time=date.today()
      print("Today's date:",today)
      d2=today.strftime("B %d,%Y")
      print("Today's Date is",d2)
      engine_talk('The todays date is')
      engine_talk(d2)

    elif 'tell me about' in command:
      name=command.replace('tell me about','')
      info=wikipedia.summary(name,1)
      print(info)
      engine_talk(info)
    
    elif 'wikipedia' in command:
      name=command.replace('wikipedia','')
      info=wikipedia.summary(name,1)
      print(info)
      engine_talk(info)
    
    elif 'what is' in command:
      name=command.replace('who is','')
      info=wikipedia.summary(name,1)
      print(info)
      engine_info(info)

    elif 'who is' in command:
      name=command.replace('who is','')
      info=wikipedia.summary(name,1)
      print(info)
      engine_talk(info)
    
    elif 'what is ' in command:
      search='https://www.google.com/seach?q='+command
      print('Here is what I found on the internet..')
      engine_talk('searching... Here is what I found on thr internet...')
      webbrowser.open(search)
    
    elif 'joke' in commmand:
      _joke=pyjokes.get_joke()
      print(_joke)
      engine_talk(_joke)
    
    elif 'search' in command:
      url="https://www.google.com/maps/search/where+am+I+?/"
      webbrowser.get().open(url)
      engine_talk("You must be somewhere near here, as per Google maps")

    elif 'locate' in command:
      engine_talk('locating....')
      loc=command.replace('locate','')
      if 'on map' in loc:
        loc=loc.replace('on map','')
      url='https://google.nl/maps/place/'+loc+'/&amp;'
      webbrowser.get().open(url)
      print('Here is the location of '+loc)
      engine_talk('Here is the location of'+loc)

    elif 'on map' in command:
      engine_talk('locating...')
      loc=command.split(" ")
      print(loc[1])
      url='https://google.nl./maps/place/'+loc[1]+'/&amp;'
      webbrowser.get().open(url)
      print('Here is the location of'+loc[1])
      engine_talk('Here is the location of'+loc[1])
    
    elif 'location of' in command:
      engine_talk('locating...')
      loc=command.replace('find location of','')
      url='https://google.nl/maps/palce/'+loc+'/&amp;'
      webbrowser.get().open(url)
      print('Here is the location of'+loc)
      engine_talk('Here is the location of '+loc)

    elif 'where is ' in command:
      engine_talk('locating...')
      loc=command.replace('where is','')
      url='https://google.nl/maps/plae/'+loc+'/&amp;'
      webbrowser.get().open(url)
      print('Here is the location of'+loc)
      engine_talk('Here is the location of'+loc)

    elif 'bootcamps' in command:
      search='http://tathastu.twowaits.in/index.html#courses'
      engine_talk('opening boot camps')
      webbrowser.open(search)

    elif 'boot camps' in command:
      search='http://tathastu.twowaits.in/index.html#courses'
      engine_talk('opening boot camps')
      webbrowser.open(search)
    
    elif 'python science bootcamp' in command:
      search='http://tathastu.twowaits.in/kickstart_data_science.html'
      engine_talk('showing data science and ml bootcamp')
      webbrowser.open(search)

    elif 'open google' in command:
      print('opening gmail...')
      engine_talk('opening google..')
      webbrowser.open_new('https://www.google.co.in/')

    elif 'gmail' in command:
      print('opening gmail...')
      engine_talk('opening gmail...')
      webbrowser.open_new('https://mail.google.com/')
    
    elif 'open youtube' in command:
      print('opening you tube...')
      engine_talk('opening you tube..')
      webbrowser.open_new('https://www.youtube.com/')
    
    elif 'open instagram' in command:
      print('opening instagram...')
      engine_talk('opening insta gram...')
      webbrowser.open_new('https://www.instagram.com/')

    elif 'open github' in command:
      print('opening git hub...')
      engine_talk('opening git hub...')
      webbrowser.open_new('https://www.github.com/')

    elif 'bye' in command:
      print('good bye, have a nice day !!')
      engine_talk('good bye, have a nice day !!')
      sys.exit()

    elif 'thank you' in command:
      print('your welcome')
      engine_talk('your welcome')
    
    elif 'stop' in command:
      print('good bye, have a nice day!!')
      engine_talk('good bye, have a nice day !!')
      sys.exit()
    
    elif 'tata' in command:
      print('good bye, have a nice day !!')
      engine_talk('good bye, have a nice day !!')
      sys.exit()
    
    else:
      print('Here is what i found on the Internet...')
      engine_talk('Here is what i found on the internet..')
      search='https://www.google.com/search?q='+command
      webbrowser.open(search)

  except Exception as ex:
    print(ex)

print('Clearing background noise...Please wait')
engine_talk('Clearing background noise... Please wait')
print('\n')
print("Hello, I am mini alexa how I can help you??")
engine_talk("Hello I am mini alexa how can I help you")

while True:
  run_alexa()
 



