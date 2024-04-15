#!/usr/bin/python3
"""A method that determines if all the boxes can be opened"""


from collections import deque

def canUnlockAll(boxes): 
    """
    Args:
        boxes (_type_): _description_
        
    Returns: True if all the boxes can be unlocked, else False
    """
    
    visited = set()
    queue = deque([0])
    
    while queue:
        current_box = queue.popleft()
        visited.add(current_box)
        
        for key in boxes[current_box]:
            if key < len(boxes) and key not in visited:
                queue.append(key)
                
    return len(visited) == len(boxes)
