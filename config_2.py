import os
BASE_DIR = "/home/rock/Desktop/Hearsight/English/set_face_who/resources"
RAW_IMG_DIR = os.path.join(BASE_DIR, "raw_images")
EMBEDDINGS_DIR = os.path.join(BASE_DIR, "embeddings")
AUDIODIR=os.path.join(BASE_DIR, "audio")
ASSISTANT_VOICE_DIR = "/home/rock/Desktop/Hearsight/audio/"
MACHINE_VOICE_DIR = "/home/rock/Desktop/Hearsight/audio/"
NO_IMG_PER_PERSON = 3



MAPPING_FILE = "mapping.json"
MAPPING_PATH = os.path.join(BASE_DIR, MAPPING_FILE)

RECOGNIZER_FILE = "recognizer.sav"
RECOGNIZER_PATH = os.path.join(BASE_DIR, RECOGNIZER_FILE)

THRESHOLD_BASE = 50

VERBOSE = True

# CAM_PORT ="libcamera-jpeg -o /home/pi/Hearsight/Tamil/Face_Recognition/1.jpg"
CAM_PORT = "ffmpeg -f v4l2 -video_size 1280x720 -i /dev/video1 -frames 1 /home/rock/Desktop/Hearsight/English/set_face_who/2.jpg"