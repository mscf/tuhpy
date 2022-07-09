import os

from record import Record

def get_records(root):
  result = []
  for f in os.walk(root):
    if Record.valid(f[0]):
      result.append(Record(f[0]))
  return result
