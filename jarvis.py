import pyttsx3
import time
import json
import os.path
import wikipedia 
converter = pyttsx3.init()
converter.setProperty('rate', 120)
converter.setProperty('volume', 1)
converter.setProperty('voice', "hindi")
print('=: Developed by Mr. Green for Linux:=')
print('=: https://github.com/iParthaSarathi/jarvis:=')
converter.say('Hi, i am jarvis, I am your new assistent')
converter.say('its nice to meet you')
converter.say('i am learning new things, help me to know more')
converter.say('please tell me your name')
converter.runAndWait()
# Data to be written x = txt.replace("bananas", "apples")
namer = input("Enter your name:")
name = namer.replace(" ", "_")
path=os.path.isfile(name+'.json')
json_object=""
res=''
detail={}
if path:
  with open(name+'.json', 'r') as openfile:
   # Reading from json file
    json_object = json.load(openfile)
    gender=""
  if json_object['gend'] != json_object['name'] :
    gender=json_object['gend']
    res=gender
    converter.say('Welcome back '+json_object['name']+", "+gender)
else :
  json_object ={
    "name" :name,
    "age" :"",
    "teach":{},
    'task' :{},
    }
  converter.say('Welcome '+name)
  converter.say('Hi '+name+' i, am, really sorry, by name, i fail to recognize your gender, please help')
  converter.runAndWait()
  gend = input("Enter your gender:")


  if( gend =='male' or gend =='Male' or gend =='MALE' ) :
      res='sir'
      json_object['gend']=res
      converter.say('thanks '+res)
      converter.runAndWait()
  elif((gend=='Female') or (gend=='Female') or (gend=='FEMALE')) :
      res='mam'
      json_object['gend']=res
      converter.say('thanks '+res)
      converter.runAndWait()
  else :
      converter.say('sorry, i can not recognize your word.')
      converter.say('let me simplify, what should i call you, sir, or, mam')
      converter.runAndWait()
      gend = input("Enter your gender: ")
      if ( gend=='sir' or gend == 'Sir' or gend == 'SIR' ) :
          res='sir'
          json_object['gend']=res
          converter.say('thanks '+res)
          converter.runAndWait()
      elif gend=='mam':
          res='mam'
          json_object['gend']=res
          converter.say('thanks '+res)
          converter.runAndWait()
      else :
          converter.say('i still face problem, to recognize, i will call you, by name, i hope, you will not fill bad')
          converter.runAndWait()
          res=name
          json_object['gend']=res
          converter.say('thanks '+res)
          converter.runAndWait()
 
with open(name+".json", "w") as outfile:
 json.dump(json_object, outfile)

t = time.localtime()
current_time = time.strftime("%H", t)
suntime =''
if int(current_time)>0 and int(current_time) <3:
 suntime='its midnight, '+res+', you should take a nap a human body need proper sleep to function'
elif int(current_time)>2 and int(current_time) <6:
 suntime='its early morning, '+res
elif int(current_time)>5 and int(current_time) <9:
 suntime='Good morning,'+res+', let"s start a amazing day'
elif int(current_time)>8 and int(current_time) <12:
 suntime='late morning '+res
elif int(current_time)>11 and int(current_time) <15:
 suntime='Good Noon '+res
elif int(current_time)>14 and int(current_time) <17:
 suntime='Good after noon'+res
elif int(current_time)>16 and int(current_time) <20:
 suntime='Good evening,'+res+", how was your day"
elif int(current_time)>19 and int(current_time) <24:
 suntime='its naight time,'+res
else :
 suntime='wish you a nice day'
print('1)type help for help\n2) type teach to teach me\n3) type exit to exit \n4)ask you want to know somthing eg: tell me about earth or  who is obama')
converter.say(suntime+',how can i help you, ')
converter.runAndWait()
lp=1
while lp==1 :
 converter.say('                    ,')
 converter.say(',I am Listening')
 converter.runAndWait()
 task=input("How can i help you:")
 if task=="help":
    converter.say('hi, i can open application for you,  i can speak with you, you can also, teach me ,you can ask me something like who is obama or tell me something ,you can tell me about your filing, give me command to continue,')
    converter.runAndWait()
 elif task=='teach' :
     tc=1
     while tc==1 :
       converter.say('what you will say to me')
       converter.runAndWait()
       tcksay=input("what you will say: ")
       converter.say('what i will reply')
       converter.runAndWait()
       tcksout=input("what i will reply: ")
       json_object['teach'][tcksay]=tcksout
       with open(name+".json", "w") as outfile:
        json.dump(json_object, outfile)
       converter.say('Want to teach more')
       converter.runAndWait()
       yn=input("Enter y for yes and n for exit: ")
       if yn=='n':
        tc=2
 elif task=='exit' :
    converter.say('thankyou ,'+res+'call me when you want tell me your name and i will recognize you')
    converter.runAndWait()
    lp=2
 else :
     #json_object['teach'][tcksay]
   if task in json_object['teach'] :
      converter.say(json_object['teach'][task]+','+res)
      converter.runAndWait()
   else :
       if ((('chrome' in task) or ('Chrome' in task) or ('CHROME' in task)) and (('open' in task) or ('run' in task) or ('Open' in task) or ('Run' in task) or ('OPEN' in task) or ('RUN' in task))):
         reslt=os.system('google-chrome')
         if reslt==0 :
          converter.say('Chrome browser is opened for you, '+res)
         else :
          converter.say('failed to open Chrome browser, '+res)
         converter.runAndWait()
       elif ((('Chromium' in task) or ('chromium' in task) or ('CHROMIUM' in task)) and (('open' in task) or ('run' in task) or ('Open' in task) or ('Run' in task) or ('OPEN' in task) or ('RUN' in task))):
         reslt=os.system('chromium-browser')
         if reslt==0 :
          converter.say('Chromium browser is opened for you, '+res)
         else :
          converter.say('failed to open Chromium browser, '+res)
          converter.runAndWait()
       elif ((('firefox' in task) or ('Firefox' in task) or ('FIREFOX' in task)) and (('open' in task) or ('run' in task) or ('Open' in task) or ('Run' in task) or ('OPEN' in task) or ('RUN' in task))):
         reslt=os.system('firefox')
         if reslt==0 :
          converter.say('Firefox browser is opened for you, '+res)
         else :
          converter.say('Failed to open firefox browser, '+res)
          converter.runAndWait()
       elif ((('text editor' in task) or ('notepad' in task) or ('Notepad' in task) or ('NOTEPAD' in task) or ('gedit' in task)or ('Gedit' in task) or ('GEDIT' in task)) and (('open' in task) or ('run' in task) or ('Open' in task) or ('Run' in task) or ('OPEN' in task) or ('RUN' in task))):
         reslt=os.system('gedit')
         if reslt==0 :
           converter.say('Gedit is opened for you, '+res)
         else :
           converter.say('Failed to open Text editor, '+res)
           converter.runAndWait()
       elif ((('vlc' in task) or ('VLC' in task) or ('Vlc' in task)) and (('open' in task) or ('run' in task) or ('Open' in task) or ('Run' in task) or ('OPEN' in task) or ('RUN' in task))):
         reslt=os.system('vlc')
         if reslt==0 :
           converter.say('VLC is opened for you, '+res)
         else :
           converter.say('Failed to open Vlc player, '+res)
           converter.runAndWait()
       elif ((('VISUAL STUDIO' in task) or ('Visual Studio' in task) or ('visual studio' in task) or ('visualstudio' in task) or ('Visualstudio' in task) or ('vscode' in task)or ('Vscode' in task)or ('VSCODE' in task)) and (('open' in task) or ('run' in task) or ('Open' in task) or ('Run' in task) or ('OPEN' in task) or ('RUN' in task))):
          reslt=os.system('code')
          if reslt==0 :
           converter.say('Chromium browser is opened for you, '+res)
          else :
           converter.say('failed to open Chromium browser,'+res)
           converter.runAndWait()
       elif (('sad' in task) or ('happy' in task) or ('Sad' in task) or ('Happy' in task)) :
          if ((('I am' in task) or ('i' in task) or ('i am' in task) or ('I AM' in task)) and (('happy' in task) or ('Happy' in task))) :    
            converter.say('nice ,'+res+', i am also happy, if you are')
            converter.runAndWait()
          elif ((('I am' in task) or ('i' in task) or ('i am' in task) or ('I AM' in task)) and (('sad' in task) or ('Sad' in task))) :    
            converter.say('why ,'+res+', anything, bad happend , dont warry all will be ok lets have some fun to refresh mood')
            converter.runAndWait()
       elif ((('I am' in task) or ('i' in task) or ('i am' in task) or ('I AM' in task)) and (('hungry' in task) or ('Hungry' in task))) :    
         converter.say('okk ,'+res+', what you like to order ')
         converter.runAndWait()
         ord=input("what you like to order or want to cook: ")
         if ((('Cooking' in ord) or ('cooking' in ord)  or ('Cook' in ord)  or ('cook' in ord)) and (('will' in ord) or ('Will' in ord) or ('should' in ord) or ('Should' in ord) or ('like' in ord) or ('like' in ord) or ('want' in ord) or ('Want' in ord) )) :    
           converter.say('so nice ,'+res+', it is a nice idea, lets cook together ')
           converter.runAndWait()
         else :
           converter.say('so nice ,'+res+', '+ord+', it must be delicious, but make sure it contain less junk ')
           converter.runAndWait()
       elif ((('r you' in task) or ('are You' in task) or ('r You' in task) or ('You are ' in task) or ('you are ' in task)) and (('sad' in task) or ('Sad' in task))) :    
          converter.say('no ,'+res+', i cant fill anything i dont have soul , but if you sad , i am also sad')
          converter.runAndWait()
       elif ((('you' in task) or ('You' in task)) and (('Hungry' in task) or ('hungry' in task))) :
          batt=os.system('upower -i $(upower -e | grep "battery") | grep --color=never -E "state|to_full|to_empty|percentage"')
          converter.say('no ,'+res+', i cant eat like human , but sir this is my battry persent, if it goes down bellow, thirty please charge me')
          converter.runAndWait()
       elif ((('tell' in task) or ('Tell' in task) or ('know' in task) or ('Know' in task)) and (('about' in task) or ('About' in task))) :
          spl=task.split('about ')
          src=wikipedia.search(spl[1],results=2)
          # src=wikipedia.suggest(src)
          ny = wikipedia.page(src)
          sum=wikipedia.summary(ny, sentences=2)
          converter.say(sum)
          converter.say('its fun,'+res+" , lets play more")
          converter.runAndWait()
       elif (('what is' in task) or ('What is' in task)or ('What are' in task)or ('what are' in task) or ('Who is' in task) or ('who is' in task) or ('who are' in task) or ('Who are' in task)) :
          spl=''
          if 'is' in task :
           spl=task.split('is ')
          else :
            spl=task.split('are ') 
          if (('You' in spl[1]) or ('you' in spl[1]) or ('YOU' in spl[1])) :
             if ((('who' in task )or ('Who' in task) or ('WHO' in task) or ('what' in task) or ('WHAT' in task) or ('What' in task) ) and (('are' in task) or ('Are' in task) or ('ARE' in task) or ('is' in task) or ('Is' in task) or ('IS' in task)) and (('you' in task) or ('YOU' in task) or ('You' in task)  or ('your' in task) or ('Your' in task) or ('YOUR' in task) or ('name' in task) or ('Name' in task) or ('NAME' in task) )) :
               converter.say('I am jarvis, Your New Assistant, '+res)
               converter.runAndWait()
          else :   
            src=wikipedia.search(spl[1],results=2)
            # src1=wikipedia.suggest(src)
            ny = wikipedia.page(src)
            sum=wikipedia.summary(ny, sentences=2)
            converter.say(sum)
            converter.say('its fun,'+res+" , lets play more")
            converter.runAndWait() 

       elif ((('who' in task )or ('Who' in task) or ('WHO' in task)) and (('create' in task) or ('Create' in task) or ('CREATE' in task))  and (('you' in task) or ('YOU' in task) or ('You' in task))) :
          converter.say('I am jarvis, Developed by Mr. Green, a,k,a, partha')
          converter.runAndWait()
       elif ((('who' in task )or ('Who' in task) or ('WHO' in task)) and (('i' in task) or ('I' in task))  and (('am' in task) or ('AM' in task) or ('Am' in task))) :
          converter.say(res+', You are ,'+name)
          converter.runAndWait()
       



#























     #
