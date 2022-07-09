import os

import edfpy

from annotation import TuarAnnotations as Annotations
from description import TuarDescription as Description

class Record:

  def __init__(self, root=None):
    self.root         = root
    self.edf          = None
    self.annotations  = None
    self.description  = None
    self.read()

  def read(self, root=None):
    if root is not None:
      self.root = root
    if self.root is not None:
      for unit in os.listdir(self.root):
        if Annotations.valid(unit):
          self.annotations = Annotations(os.path.join(self.root, unit))
        elif Description.valid(unit):
          self.description = Description(os.path.join(self.root, unit))
        elif os.path.splitext(unit)[-1] == ".edf":
          self.edf = edfpy.Reader.open(os.path.join(self.root, unit))

  @classmethod
  def valid(cls, path):
    result = True
    for f in list(os.listdir(path)):
      if Annotations.valid(f) or Description.valid(f) or os.path.splitext(f)[-1] == ".edf":
        continue
      else:
        result = False
    return result
      
   
