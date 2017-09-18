"""models for use in other scripts"""

class Team(object): # new style class inherits from object
    """my team class"""
    def __init__(self, name, mascot, wins):
        self.name = name
        self.mascot = mascot
        self.wins = wins
        print "__name__ from team", __name__

class School(object): # new style class inherits from object
    """my school class"""
    def __init__(self, name, enrollment):
        self.name = name
        self.enrollment = enrollment

class Article(object):
    """something i copied from stack overflow"""
    def __init__(self, name, available):
        self._name = name
        self.available = available
        self._available = available

    @property
    def name(self):
        """the name property"""
        return self._name
