import os

MODEL_URL = "http://alphacephei.com/vosk/models/vosk-model-small-en-in-0.4.zip"
BASE_DIR = "resources"
MODEL_FILE_ZIP = os.path.join(BASE_DIR, "recognizer.zip")

LANG_FILE = "/home/rock/Desktop/Hearsight/lang.txt"

MODEL_FILE = "vosk-model-small-en-in-0.4"

COMMANDS = [
    "walk", "walking", "marking", "king", "barking", "parking", "go see", "gosee", "what", "money", "person", "per son", "colors", "color", "colours",
    "colour", "carla", "carlos", "caller", "corner", "colar", "read", "up", "application", "app", "storage", "time", "date", "time and date",
    "time a date", "time an date", "set", "settings", "thing", "letting thing", "of", "off", "wait", "weight", "right", "way it", "out"
]

MAX_ATTEMPT = 2

#"walk", "walking", "marking", "king", "barking", "parking", "go see", "gosee", "what", "money", "person", "per son", "colors", "color", "colours",
#"colour", "carla", "carlos", "caller", "corner", "colar", "read", "up", "application", "app", "storage", "time", "date", "time and date",
#"time a date", "time an date", "set", "settings", "thing", "letting thing", "of", "off", "wait", "weight", "right", "way it", "out"

#    "person", "walking", "money", "of", "walk",
#    "what", "time", "read", "go see", "out", "set",  
#    "parking", "marking", "per son", "storage",
#    "off", "colors", "color", "colours", "wait", "weight", 
#    "colour", "carla", "carlos", "caller", "corner", "colar",  
#    "up", "application", "app", "right", "settings",
#    "barking", "date","time and date",
#    "time a date", "time an date", "gosee",
#    "way it", "king", "thing",
#    "letting thing"

#COMMANDS = [
#    "person", "walking", "money", "of", "media", "walk",
#    "document", "what", "time", "read", "go see", "out",
#    "add face", "add", "face","set", "phase", "add phase",  
#    "parking", "marking", "per son", "who", "who is this",
#    "identify", "recognize", "recognition", "identification", 
#    "off", "colors", "color", "colours", "wait", "weight", 
#    "colour", "carla", "carlos", "caller", "corner", "colar",  
#    "up", "application", "app", "how to use", "right", "settings",
#    "how two use", "barking", "guide", "date","time and date",
#    "time a date", "time an date", "mobile", " mobile up", "gosee",
#    "mobile application", "mobile app", "way it", "king", "thing",
#    "letting thing"
#]


#COMMANDS = [
#    "change language", "person", "walking", "money", "of", "media",
#    "document", "temperature", "what", "time", "read", "go see", "out",
#    "add face", "add", "face","set", "phase", "add phase", "walk", 
#    "parking", "marking", "per son", "who", "who is this",
#    "identify", "recognize", "recognition", "identification", "king",
#    "language", "off", "device temperature", "colors", "color", "colours",
#    "colour", "carla", "carlos", "caller", "corner", "colar", "gosee", 
#    "up", "application", "app", "user", "user guide", "how to use",
#    "how two use", "barking", "guide", "date","time and date",
#    "time a date", "time an date", "mobile", " mobile up",
#    "mobile application", "mobile app", "volume", "battery", "level",
#    "battery level", "three level", "that ray", "that level", "way it",
#    "wait", "weight", "right", "settings"
#]

#COMMANDS = [
#    "change language", "person", "walking", "money", "of", "media",
#    "document", "temperature", "what", "time", "read", "go see", "out",
#    "set face", "said face", "face","set", "phase", "walk", 
#    "parking", "marking", "per son", "who", "who is this",
#    "identify", "recognize", "recognition", "identification", "king",
#    "language", "off", "device temperature", "colors", "color", "colours",
#    "colour", "carla", "carlos", "caller", "corner", "colar", "gosee", 
#    "up", "application", "app", "user", "user guide", "how to use",
#    "how two use", "barking", "guide", "date","time and date",
#    "time a date", "time an date", "mobile", " mobile up",
#    "mobile application", "mobile app", "volume", "battery", "level",
#    "battery level", "three level", "that ray", "that level", "way it",
#    "wait", "weight", "right"
#]

#COMMANDS = [
#    "change language", "person", "walking", "money", "of", "media",
#    "document", "temperature", "what", "time", "read", "go see", "out",
#    "set face", "said face", "face","set", "phase", "walk", 
#    "parking", "marking", "per son", "who", "who is this",
#    "identify", "recognize", "recognition", "identification", "king",
#    "language", "off", "device temperature", "colors", "color", "colours",
#    "colour", "carla", "carlos", "caller", "corner", "colar", "gosee", 
#    "up", "application", "app", "user", "user guide", "how to use",
#    "how two use", "barking", "guide", "date","time and date",
#    "time a date", "time an date", "mobile", " mobile up",
#    "mobile application", "mobile app", "volume", "battery", "level",
#    "battery level", "three level", "that ray", "that level"
#]

#COMMANDS = [
#    "change language", "person", "walking", "money", "of", "media",
#    "document", "temperature", "what", "time", "read", "go see", "out",
#    "set face", "that face", "said face", "face","set", "phase", "walk", 
#    "parking", "marking", "per", "son", "per son", "who", "who is this",
#    "identify", "recognize", "recognition", "identification", "king",
#    "language", "off", "device temperature", "colors", "color", "colours",
#    "colour", "carla", "carlos", "caller", "corner", "colar", "gosee", 
#    "up", "application", "app", "user", "user guide", "how to use",
#    "how two use", "barking", "guide", "date","time and date",
#    "time a date", "time an date", "mobile", " mobile up",
#    "mobile application", "mobile app", "volume"
#]

#COMMANDS = [
#    "change language", "person", "walking", "money", "of", "media",
#    "document", "temperature", "what", "time", "read", "go see", "out",
#    "set face", "that face", "said face", "face","set", "phase", "walk", 
#    "parking", "marking", "per", "son", "per son", "who", "who is this",
#    "identify", "recognize", "recognition", "identification", "king",
#    "language", "off", "device temperature", "colors", "color", "colours",
#    "colour", "carla", "carlos", "caller", "corner", "colar", "gosee", 
#    "up", "application", "hearsight", "here", "site", "here site",
#    "here set", "here site up", "here site application", "app", "user", 
#    "user guide", "how to use", "how two use", "barking", "guide", "date",
#    "time and date", "time a date", "time an date"
#]


#COMMANDS = [
#    "change language","person", "walking", "money", "of", "media",
#    "document", "temperature", "what", "time", "read", "go see", "out",
#    "set face","that face","said face","face","set","phase","walk", "barking",
#    "parking", "marking", "per", "son", "per son", "who", "who is this", "king",
#    "who are you", "identify", "recognize", "recognition", "identification",
#    "language", "off", "device temperature", "colors", "color", "colours",
#    "colour", "carla", "carlos", "caller", "rainbow", "corner", "colar", 
#    "gosee", "up", "application", "hearsight", "here", "site", "here site",
#    "here set", "here site up", "here site application", "app"
#]


#COMMANDS = [
#    "change language","person", "walking", "money", "of", "bank", "work sheet",
#    "document", "temperature", "what", "time", "book", "read", "go see", "out",
#    "set face","that face","said face","face","set","phase","walk", "barking",
#    "parking", "marking", "per", "son", "per son", "who", "who is this", "king",
#    "who are you", "identify", "recognize", "recognition", "identification",
#    "language", "off", "device temperature", "worksheet", "colors", "color",
#    "colours", "colour", "carla", "carlos", "caller", "rainbow", "corner",
#    "colar", "gosee"   
#]


#COMMANDS = [
#    "change language", "person", "walking", "money", "of", "media",
#    "document", "temperature", "what", "time", "read", "go see", "out",
#    "set face", "that face", "said face", "face","set", "phase", "walk", 
#    "parking", "marking", "per", "son", "per son", "who", "who is this",
#    "identify", "recognize", "recognition", "identification", "king",
#    "language", "off", "device temperature", "colors", "color", "colours",
#    "colour", "carla", "carlos", "caller", "corner", "colar", "gosee", 
#    "up", "application", "app", "user", "user guide", "how to use",
#    "how two use", "barking", "guide", "date","time and date",
#    "time a date", "time an date", "mobile", " mobile up",
#    "mobile application", "mobile app", "volume", "scan", "can"
#]