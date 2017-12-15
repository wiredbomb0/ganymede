r = [64, 128, 255]
g = [64, 128, 255]
b = [64, 128, 255]

for _r in r:
  for _g in g:
    for _b in b:
      col_light = "rgb({}, {}, {})".format(_r, _g, _b)
      col_dark  = "rgb({}, {}, {})".format(_r / 4, _g / 4, _b / 4)
      print """<span style="background-color: {}; color: {}; border: 1px solid {}">Scroll of Wisdom</span><br>""".format(col_dark, col_light, col_light)
      