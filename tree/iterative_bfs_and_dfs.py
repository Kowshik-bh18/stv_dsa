#dfs -> stack
def dfs(root):
    stack = [root]

    while stack:
        node = stack.pop()
        print(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

#bsf ->queue
from collections import deque

def level_order(root):
    q = deque([root])
    
    while q:
        node = q.popleft()
        print(node.val)
        
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)