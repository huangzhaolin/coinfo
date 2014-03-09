__author__ = 'zhaolinhuang'
import hashlib
def md5Encode(string):
    if string==None:
        return None
    md5=hashlib.md5()
    md5.update(string)
    return md5.hexdigest()

