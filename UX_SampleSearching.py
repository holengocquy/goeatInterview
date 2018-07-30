#UX searching GoEat
from anytree import Node, RenderTree, AsciiStyle
from anytree.search import find_by_attr
#tags defining
def initTag(root):
    #init ingredients of tree from root
    print("===Tags Defining===")
    print("Please enter the Tag and its Parent\n")
    while True:
        inputTagParent = input("Enter Tag Parent : ")
        inputTag = input("Enter Tag : ")
        currentTag = find_by_attr(root, inputTagParent)
        if currentTag == None:
            tagParent = Node(inputTagParent, parent=root)
            tagName = Node(inputTag, parent=tagParent)            
        else:
            tagName = Node(inputTag, parent=find_by_attr(root, inputTagParent))                        
        
        print("Press any key except '0' to continue enter tags")
        if input("Your choice : ") == "0":
            break
        

def printContent(root, tagName):
    print("Result from tag #"+tagName)
    if find_by_attr(root, tagName).is_leaf:
        print(tagName)
    else:
        tagChild = find_by_attr(root, tagName).children
        for contentNode in tagChild:
            #get position for formating output
            x = str(contentNode).rfind('/')
            y = str(contentNode).rfind('\'')
            contentData = str(contentNode)
            if contentNode.is_leaf:            
                print(contentData[x+1: y])
            else:
                printContent(contentNode, contentData[x+1: y])      

#Implementation...
root = Node("gastronomy")

initTag(root)

#print content from tag
tag = input("Enter tag to print its content :")
printContent(root, tag)

#build a visible tree
print("\n---Information of all tags---")
print(RenderTree(root, style=AsciiStyle()).by_attr())
