import re

def checkio(data):
    if data.isalnum() and len(data)>=10 and (re.search('[A-W]',data) != None) and (re.search('[a-w]',data) != None):
        return True
    else:
        return False

checkio("A1213pokl")
