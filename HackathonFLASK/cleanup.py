import shutil
import os

dir_name = os.path.dirname(os.path.realpath(__file__)) + '/static/temp'

shutil.rmtree(dir_name)
print("TEMP DIRECTORY DELETED")


if not os.path.exists(dir_name):
    os.makedirs(dir_name)

print("TEMP DIRECTORY RE-CREATED")


