import pystache

def create_color_statements(r, g, b):
  light = "{} {} {}".format(r, g, b)
  dark  = "{} {} {}".format(int(r/4), int(g/4), int(b/4))

  s = """SetTextColor {{light}}
  SetBorderColor {{light}}
  SetBackgroundColor {{dark}}"""

  return pystache.render(s, {"light": light, "dark": dark})
