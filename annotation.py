import csv
import os


class Annotation:

  def __init__(self, channel, start, stop, label, confidence):
    self.channel    = channel
    self.start      = float(start)
    self.stop       = float(stop)
    self.label      = label
    self.confidence = float(confidence)

  def __str__(self):
    return f"channel: {self.channel}, " \
           f"start: {self.start}, " \
           f"stop: {self.stop}, " \
           f"label: {self.label}, " \
           f"confidence: {self.confidence}"


class Annotations:

  def __init__(self, root=None):
    self.root         = root
    self.annotations  = []
    self.read()

  def read(self, root=None):
    if root is not None:
      self.root = root
    if self.root is not None:
      for r in csv.DictReader(filter(lambda row: row[0] != "#", open(self.root, newline=""))):
        self.annotations.append(Annotation(r["channel"],
                                           r["start_time"],
                                           r["stop_time"],
                                           r["label"],
                                           r["confidence"]))

  @classmethod
  def valid(cls, path):
    raise NotImplementedError


class TuarAnnotations(Annotations):

  file_extension = ".csv"

  def __init__(self, root=None):
    if root is not None:
      if not self.valid(root):
        root = None
    super().__init__(root)

  @classmethod
  def valid(cls, path):
    return os.path.splitext(path)[-1] == cls.file_extension
