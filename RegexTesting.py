import re

string = '''Love, Kenneth: 20
Chalkley, Andrew: 25
McFarland, Dave: 10
Kesten, Joy: 22
Stewart Pinchback, Pinckney Benton: 18'''

players = re.search('''
                    ^(?P<last_name>[\w ]+),\s
                    (?P<first_name>[\w ]+):\s
                    (?P<score>\d{2})$''', string, re.X|re.M)

class Player:
  def __init__(self,**kwargs):
    self.last_name = players.group('last_name')
    self.first_name = players.group('first_name')
    self.score = players.group('score')
