import re


def epc_format(s):
    s = re.sub('\W+', ' ', s)
    s = s.lower()
    return s