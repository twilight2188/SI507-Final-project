
from rawg import *
import json
import ast
#
# The following two trees are useful for testing.
#
smallTree = \
    ("Are you playing on your PC/XBOX? ",
        ({'name': 'Elden Ring', 'release_year': '2022', 'metacritic': 96, 'image': 'https://media.rawg.io/media/games/5ec/5ecac5cb026ec26a56efcc546364e348.jpg', 'rating': 95.8543359076352, 'summary': 'Elden Ring is a fantasy, action and open world game with RPG elements such as stats, weapons and spells. Rise, Tarnished, and be guided by grace to brandish the power of the Elden Ring and become an Elden Lord in the Lands Between.', 'url': 'https://www.igdb.com/games/elden-ring'}, None, None),
        ({'name': 'The Legend of Zelda: Breath of the Wild', 'release_year': '2017', 'metacritic': 97, 'image': 'https://media.rawg.io/media/games/cc1/cc196a5ad763955d6532cdba236f730c.jpg', 'rating': 94.83972272696695, 'summary': 'In this 3D open-world entry in the Zelda series, Link is awakened from a deep slumber without his past memories in the post-apocalyptic Kingdom of Hyrule, and sets off on a journey to defeat the ancient evil Calamity Ganon. Link treks, climbs and glides through fields, forests and mountain ranges while meeting and helping friendly folk and defeating enemies in order to gather up the strength to face Ganon.', 'url': 'https://www.igdb.com/games/the-legend-of-zelda-breath-of-the-wild'}
        , None, None))
def main():
    """Main Function for 20 Questions"""
    # Write the "main" function for 20 Questions here.  Although
    # main() is traditionally placed at the top of a file, it is the
    # last function you will write.
    print('Welcome to My Game Engine!\n')
    option = input('Which option do you want ? \n1. Game Search\n2. Game Recommendation\n')
    if(option == '1'):
        search()
    elif(option == '2'):
        load = yes('Would you like to load a tree from a file?')
        if(load):
            filename = input("What's the name of the file?")
            treeFile = open(filename, 'r')
            tree = loadTree(treeFile)
            treeFile.close()
        else:
            tree = smallTree
        while True:
            tree = play(tree)
            if(yes('Would you like to play again?') == False):
                break
        if(yes('Would you like to save this tree for later?')):
            filename = input('Please enter a file name: ')
            treeFile = open(filename, 'w')
            saveTree(tree, treeFile)
            treeFile.close()
            print('Thank you! The file has been saved.')
        print('Bye!')

def simplePlay(tree):
    """plays the game once by using the tree to guide its questions.
       Return true if guess the correct answer
       Return flase if not guess the correct answer"""
    text, left, right = tree
    if isLeaf(tree):
        return yes(f"Is it {text}?")
    elif yes(text):
        return simplePlay(left)
    else:
        return simplePlay(right)
def play(tree):
    """plays the game once by using the tree to guide its questions. However.
       Returns a new tree that is the result of playing the game on the original tree and learning from the answer"""
    text, left, right = tree
    if isLeaf(tree):
        return playleaf(tree)
    elif yes(text):
        subtree = play(left)
        return(text,subtree,right)
    else:
        subtree = play(right)
        return(text,left,subtree)

def isLeaf(tree):
    text, left, right = tree
    if left is None  and  right is None:
        return True
    else:
        return False
def yes(prompt):
    answer = input(prompt).lower()
    if(answer == 'yes'or answer == 'y'or answer == 'yup'or answer == 'sure'):
        return True
    elif (answer == 'no'or answer == 'n'or answer == 'nah'or answer == 'nope'):
        return False
    else:
        return yes("Please enter 'yes' or 'no': ")
def playleaf(tree):
    text, left, right = tree
    text = ast.literal_eval(text)
    answer = yes(f"Is it {text['name']}?")
    if(answer == True):
        print('I got it!')
        return tree
    elif(answer == False):
        item = input('Drats! What was it?')
        item = ast.literal_eval(item)
        question = input(f"What's a question that distinguishes between {item['name']} and {text['name']}?")
        new_answer = yes(f"And what's the answer for {item['name']}?")
        if new_answer == True:
            return (question,(item, None, None),(text, None, None))
        elif new_answer == False:
            return (question,(text, None, None),(item, None, None))
def saveTree(tree, treeFile):
    text, left, right = tree
    if isLeaf(tree):
        print('Leaf',file = treeFile)
        print(text, file = treeFile)
    else:
        print('Internal node', file = treeFile)
        print(text,file = treeFile)
        saveTree(left, treeFile)
        saveTree(right, treeFile)
def loadTree(treeFile):
    lines = treeFile.readlines()
    lines = [line.strip() for line in lines]
    return load(lines)[0]
def load(list):
    if list[0] == 'Leaf':
        return (list[1],None,None),list[2:]
    elif list[0] == 'Internal node':
        a,b = load(list[2:])
        c,d = load(b)
        return(list[1],a,c), d
#
# The following two-line "magic sequence" must be the last thing in
# your file.  After you write the main() function, this line it will
# cause the program to automatically play 20 Questions when you run
# it.
#
if __name__ == '__main__':
    main()