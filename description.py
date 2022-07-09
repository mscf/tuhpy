import os


class Description:

  def __init__(self, root=None):
    self.root     = root
    self.details  = None
    self.read()

  def read(self, root=None):
    if root is not None:
      self.root = root
    if self.root is not None:
      #print(self.root)
      self.details = open(self.root, "r", encoding="ISO-8859-1").read()

  @classmethod
  def valid(self, path):
    raise NotImplementedError

class TuarDescription(Description):

  file_extension = ".txt"

  def __init__(self, root=None):
    if root is not None:
      if not self.valid(root):
        root = None

    super().__init__(root)

  @classmethod
  def valid(cls, path):
    return os.path.splitext(path)[-1] == cls.file_extension
