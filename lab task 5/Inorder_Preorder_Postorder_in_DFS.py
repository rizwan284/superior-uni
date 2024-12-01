# Research about "Inorder, Preorder, Postorder" and implement in DFS

tree = {
    'A' : ['B', 'C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'G'],
    'D' : [],
    'E' : [],
    'F' : [],
    'G' : [],
}


def inorder(node):
    if node:
        for child in tree[node][:1]:  
            inorder(child)
        print(node, end=' ') 
        for child in tree[node][1:]:  
            inorder(child)

def preorder(node):
    if node:
        print(node, end=' ')  
        for child in tree[node]:  
            preorder(child)

def postorder(node):
    if node:
        for child in tree[node]:  
            postorder(child)
        print(node, end=' ') 

print("\nInorder: ")
inorder('A')

print("\nPreorder: ")
preorder('A')

print("\nPostorder: ")
postorder('A')


