""" Application configuration"""
import os

DEBUG = True
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'img')
CACHE_TYPE = "null"

