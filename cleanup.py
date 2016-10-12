import shutil
import os

dir_name = os.path.dirname(os.path.realpath(__file__)) + '/static/temp'

shutil.rmtree(dir_name)

print("TEMP DIRECTORY EMPTIED")
