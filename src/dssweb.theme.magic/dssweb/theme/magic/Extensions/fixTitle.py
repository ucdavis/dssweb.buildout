import re

def fixTitle(strid):
     cleanString = re.sub('\W+','-',strid)
     return cleanString
