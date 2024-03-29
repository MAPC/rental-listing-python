"""
  Organize environment variables into an 
  accessible static object.
"""

from os import environ, path
from munch import Munch
from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv())


paths = Munch({
  'DATA': environ.get('DATA_PATH'),
  'SPATIAL': environ.get('SPATIAL_DATA_PATH'),
  'OUTPUT': environ.get('OUTPUT_PATH'),
})

files = Munch({
  'LISTINGS': environ.get('LISTINGS_FILE'),
})
