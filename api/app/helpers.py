import hashlib


def text_to_md5(text):
  return hashlib.md5(text.encode('utf-8')).hexdigest()
