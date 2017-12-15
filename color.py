class Color:
  R = 0
  G = 0
  B = 0
  
  def __init__(self, r, g, b):
    self.R = r
    self.G = g
    self.B = b
    
  def __repr__(self):
    return "{} {} {}".format(self.R, self.G, self.B)