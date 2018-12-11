import os
import math
import shutil

from helper import create_color_statements
from datetime import datetime
from string import Template

BUILD_VERSION = "0.1.0-pre"

if __name__ == "__main__":
  file_list = []
  for file in os.listdir("./divs"):
    if file.endswith(".template"):
      file_list.append(os.path.join("./divs", file))

  file_list = sorted(file_list)

  complete_text = ""
  for file in file_list:
    # Open the template and read
    with open(file, "r") as _f:
      s = Template(_f.read())

    # Perform the magic!
    result = s.substitute({
      "BUILD_VERSION": BUILD_VERSION,
      "BUILD_DATE": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),

      "COLOR_EQUIPMENT_NORMAL": create_color_statements(200, 200, 200),
      "COLOR_EQUIPMENT_MAGIC": create_color_statements(136, 136, 255),
      "COLOR_EQUIPMENT_RARE": create_color_statements(255, 255, 119),
      "COLOR_EQUIPMENT_UNIQUE": create_color_statements(175, 96, 37),
      "COLOR_EQUIPMENT_VALUABLE": create_color_statements(119, 119, 255),
      "COLOR_EQUIPMENT_SHAPED": create_color_statements(128, 64, 128),
      "COLOR_EQUIPMENT_CHROMATIC": create_color_statements(128, 128, 128),

      "COLOR_LEAGUE_SPECIFIC": create_color_statements(255, 165, 0),
      "COLOR_QUEST_ITEM": create_color_statements(74, 230, 58),
      "COLOR_CURRENCY": create_color_statements(170, 158, 130),
      "COLOR_DIVINATION_ITEM": create_color_statements(14, 186, 255),
      "COLOR_GEMS": create_color_statements(27, 162, 155),
      "COLOR_MAPS": create_color_statements(210, 0, 220),
      "COLOR_LABYRINTH": create_color_statements(254, 179, 37),

      "COLOR_REMAINING": create_color_statements(255, 255, 255)
    })
    
    complete_text += result.rstrip() + "\n\n"
  complete_text = complete_text.rstrip() + "\n"

  # Open the output and write
  with open("ganymede.filter", "w") as _f:
    _f.write(complete_text)

  # Copy all required files  
  path_poe = os.path.expanduser('~\\My Documents\\My Games\\Path of Exile\\')
  shutil.copy("ganymede.filter", path_poe)  
