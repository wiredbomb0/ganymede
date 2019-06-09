import os
import shutil
import pystache

from stat import S_IREAD, S_IWUSR
from datetime import datetime

from lib import create_color_statements

FILE_FILTER_OUTPUT = "ganymede.filter"

stache = {
  "BuildTime": datetime.utcnow(),
  "Currency": create_color_statements(170, 158, 130),
  "Divination": create_color_statements(14, 186, 255),
  "Gem": create_color_statements(27, 162, 155),
  "ShapedItem": create_color_statements(128, 64, 128),
  "Quest": create_color_statements(74, 230, 58),
  "Labyrinth": create_color_statements(254, 179, 37),
  "Chromatic": create_color_statements(100, 100, 100),
  "Flask": create_color_statements(150, 33, 72),
  "Maps": create_color_statements(244, 137, 66),
  "EquipmentValuable": create_color_statements(119, 119, 255),
  "EquipmentNormal": create_color_statements(200, 200, 200),
  "EquipmentMagic": create_color_statements(136, 136, 255),
  "EquipmentRare": create_color_statements(255, 255, 119),
  "EquipmentUnique": create_color_statements(175, 96, 37),
  "LeagueSpecific": create_color_statements(75, 160, 180),
  "Catch": create_color_statements(1, 1, 1)
}

# Generate list of all sections to be merged
file_list = []
for file in os.listdir("./sections"):
  if file.endswith(".template"):
    file_list.append(os.path.join("./sections", file))

# Load all template files and join them all together
complete_text = ""
for file in file_list:
  with open(file, "r") as _f:
    complete_text += _f.read() + "\n"

# Open filter file for editing
if os.path.isfile(FILE_FILTER_OUTPUT):
  os.chmod(FILE_FILTER_OUTPUT, S_IWUSR|S_IREAD)

with open(FILE_FILTER_OUTPUT, "w") as _f:
  _f.write(pystache.render(complete_text, stache))

# Copy file as required
path_poe = os.path.expanduser("~\\My Documents\\My Games\\Path of Exile\\")
path_audio = os.path.expanduser("~\\My Documents\\My Games\\Path of Exile\\audio")
if not os.path.exists(path_audio):
  os.makedirs(path_audio)

# Copy audio from folder
shutil.copy(FILE_FILTER_OUTPUT, path_poe)
for file in os.listdir("./audio"):
  shutil.copy(os.path.join("./audio", file), path_audio)

# Make the local file read-only so no accidental edits
os.chmod(FILE_FILTER_OUTPUT, S_IREAD)
