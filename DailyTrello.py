##Author: Jared Raiola
##
##Personal Use -- Hence when api_key, api_secret, and token are all in plain sight
##
##py-trello documentation: https://readthedocs.org/projects/py-trello-dev/downloads/pdf/latest/
##Big thanks to those who wrote that documentation, it's super helpful

from trello import TrelloClient
from datetime import date
import datetime
import os
import sys

##Create class DailyTrello for executable use
##Make an executable using pyinstaller!
class DailyTrello(object):

    ##Init Trello connection
    def __init__(self):
        self.client = TrelloClient(
            api_key='XXXXXX',
            api_secret='XXXXXX',
            token='XXXXXX'
        )

    ##Access specific board and specific board list.
    ##I already knew my list id so I was able to use get_list
    def accessBoards(self):
        boards = self.client.list_boards()
        for b in boards:
            if b.name == "ToDo":
                board = b
                ##List id is the XXXXX param
                edit = board.get_list("XXXXX")
                return edit
        return None

    ##Other solution if ID is not known
    """
    def accessBoards(self):
        boards = self.client.list_boards()
        for b in boards:
            if b.name == "ToDo":
                board = b
                ############################
                ##None is the filter, some filter must be included
                lists = board.get_lists(None)
                ############################
                for list in lists:
                    if list.name == "THE LIST YOU'RE LOOKING FOR":
                        return list
        return None
    """

    ##How to find list ID
    """
    def findListID(self):
        boards = client.list_boards()
        for b in boards:
            if b.name == "ToDo":
                board = b
                ############################
                ##None is the filter, some filter must be included
                lists = board.get_lists(None)
                ############################
                for aList in lists:
                    if aList.name == "NAME OF LIST":
                        ################
                        print(aList.id)
                        ################
    """

    def dailyCheck(self):
        exeLoc = os.path.dirname(os.path.realpath(sys.argv[0]))
        os.chdir(exeLoc)
        os.chdir('..')
        os.chdir('..')
        fin = open(os.getcwd() + "\\cardData\\data.txt","r")
        lines = fin.readlines()
        fin.close()
        lines = [line.strip() for line in lines]
        ## second element is the date

        ## date.today() > datetime.datetime.strptime(lines[1],'%Y-%m-%d').date()
        ## check for new day
        
        if date.today() > datetime.datetime.strptime(lines[1],'%Y-%m-%d').date():
            fout = open(os.getcwd() + "\\cardData\\data.txt", "w")
            fout.write("Date:\n" + str(date.today()))
            fout.close()

            edit = self.accessBoards()

            try:
                fin = open(os.getcwd() + "\\cardData\\RepeatCards.txt", "r")
                cards = fin.readlines()
                cards = [card.strip() for card in cards]
                for c in cards:
                    edit.add_card(c)
            except:
                pass


if __name__ == '__main__':
    DailyTrello().dailyCheck()
