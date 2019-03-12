from string import Template

def create_color_statements(r, g, b):
  light = "{} {} {}".format(r, g, b)
  dark  = "{} {} {}".format(int(r/4), int(g/4), int(b/4))

  s = Template("""SetBorderColor $LIGHT
  SetTextColor $LIGHT
  SetBackgroundColor $DARK""")

  return s.substitute({
    "LIGHT": light,
    "DARK": dark
  })
