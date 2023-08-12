import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
voices=engine.getProperty ('voices')
# engine.setProperty('voice', "french") 

## You can find all the available voices in the voices.txt file, all you have to do is change the second parameter of the line above to the id of the voice you would like to use as per the example above.

engine.say('Sally sells seashells by the seashore.')
engine.say('The quick brown fox jumped over the lazy dog.')

# engine.say('bonjour les amis.')
engine.runAndWait()