from rawg import *
import ast
#
# The following two trees are useful for testing.
#
def main():
    print('Welcome to My Game Engine!\n')
    option = input('Which option do you want ? \n1. Game Search\n2. Game Recommendation\n')
    if(option == '1'):
        search()
    elif(option == '2'):
        filename = 'tree.txt'
        treeFile = open(filename, 'r')
        tree = loadTree(treeFile)
        treeFile.close()
        while True:
            tree = play(tree)
            if(yes('Would you like to play again?') == False):
                break
        print('Bye!')
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
    print(f"The recommendation for you is {text['name']}\n")
    answer = yes('Do you want more info?')
    if(answer == True):
        detail(text)
    return tree
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