color_swap = {
  "@COLOR_QUEST_LIGHT": "74 230 58",
  "@COLOR_QUEST_DARK":  "18 57 14"
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