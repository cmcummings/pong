# res.py
# Functions for loading resources
import os, pygame
from config import RESOURCE_DIR


def load_resource(file_name):
    return pygame.image.load(os.path.join(RESOURCE_DIR, file_name))
