def loadTree(treeFile):
    lines = treeFile.readlines()
    lines = [line.strip() for line in lines]
    return load(lines)[0]