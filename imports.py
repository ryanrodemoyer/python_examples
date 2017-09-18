"""test code on imports"""

from models import Team, Article

def use_articles():
    """using my articles brah"""
    article = Article("python for rooks", True)
    article._name = "my new name" # guess this is a warning about protected member but you can still do it
    article.available = False
    article._available = True
    print article.name

def main():
    """my main function"""
    print "__name__ from imports", __name__
    some_team = Team("atlanta", "falcons", 2)

    print some_team.name
    print some_team.mascot
    print some_team.wins

    some_team.wins = 3

    print some_team.wins

use_articles()
