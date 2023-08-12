import configparser
import os
import time

import pyttsx3

engine = pyttsx3.init()

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)


# Define the path to the config.conf file
config_file = "config.conf"

# Create a ConfigParser instance and read the config file
config = configparser.ConfigParser()
config.read(config_file)

# Access the parameters
files_path = config.get("parameters", "FOLDER_PATH")

# Print the parameters
print("PARAMETER_1:", files_path)

print(os.getcwd())

sources = ["Anime", "Series", "Movies"]
path_existence=[]
for s in sources:
    filepath = os.path.join(files_path, s)
    if (os.path.exists(filepath)):
        print(s+" exists.")
        if not (os.path.isfile(filepath)):
            print(" And it is indeed a folder.")
            path_existence.append(s)
        else:
            print(" But it is not a folder.")       
    else:
        print(s+ " doesn't exist")
        # print("Which of the folders would you like to create?")


engine.say('The existing folders are the following: ')
time.sleep(0.5)
for pe in path_existence:
    engine.say(pe)
    time.sleep(0.5)
time.sleep(0.5)
engine.say('What would you like to watch ?')
engine.runAndWait()