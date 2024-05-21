import os
BASE_DIR = "resources"
RAW_IMG_DIR = os.path.join(BASE_DIR, "raw_images")
EMBEDDINGS_DIR = os.path.join(BASE_DIR, "embeddings")
NO_IMG_PER_PERSON = 3

MAPPING_FILE = "mapping.json"
MAPPING_PATH = os.path.join(BASE_DIR, MAPPING_FILE)

RECOGNIZER_FILE = "recognizer.sav"
RECOGNIZER_PATH = os.path.join(BASE_DIR, RECOGNIZER_FILE)

THRESHOLD_BASE = 50

VERBOSE = True

CAM_PORT = 0