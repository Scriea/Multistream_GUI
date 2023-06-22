import os
import sys
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STREAM_SOURCES = os.path.join(ROOT,'stream.txt')

def get_stream_list(source = STREAM_SOURCES):
    file = open(source, 'r')
    stream_list = file.readlines()
    return stream_list
