color_swap = {
  "@COLOR_QUEST_LIGHT": "74 230 58",
  "@COLOR_QUEST_DARK":  "18 57 14",
  
  "@COLOR_DIVINATION_LIGHT": "14 186 255",
  "@COLOR_DIVINATION_DARK":  "3 46 63",
  
  "@COLOR_CURRENCY_LIGHT": "170 158 130",
  "@COLOR_CURRENCY_DARK":  "42 39 32",
  
  "@COLOR_MAP_LIGHT": "210 0 220",
  "@COLOR_MAP_DARK":  "52 0 55",
  
  "@COLOR_ITEM_UNIQUE_LIGHT": "175 96 37",
  "@COLOR_ITEM_UNIQUE_DARK":  "44 24 9",

  "@COLOR_ITEM_RARE_LIGHT": "255 255 119",
  "@COLOR_ITEM_RARE_DARK":  "64 64 30",

  "@COLOR_ITEM_MAGIC_LIGHT": "136 136 255",
  "@COLOR_ITEM_MAGIC_DARK":  "34 34 64",

  "@COLOR_ITEM_NORMAL_LIGHT": "200 200 200",
  "@COLOR_ITEM_NORMAL_DARK":  "50 50 50",
  
  "@COLOR_ITEM_SOCKETS_LIGHT": "119 119 255",
  "@COLOR_ITEM_SOCKETS_DARK":  "30 30 64",
  
  "@COLOR_GEM_LIGHT": "27 162 155",
  "@COLOR_GEM_DARK":  "6 40 38",
  
  "@COLOR_ESSENCE_LIGHT": "255 165 0",
  "@COLOR_ESSENCE_DARK": "63 41 0",
  
  "@COLOR_SHAPED_LIGHT": "128 64 128",
  "@COLOR_SHAPED_DARK":  "32 16 32"
}

item_filter = None
# Open file
with open("valkyrie.filterplus", "r") as _f:
  item_filter = _f.read()
  
# Replace all the colors
for key, value in color_swap.iteritems():
  item_filter = item_filter.replace(key, value)
  
# Write file
with open("valkyrie.filter", "w+") as _f:
  _f.write(item_filter)