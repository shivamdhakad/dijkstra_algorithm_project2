import cv2
import numpy as np
import heapq as hq
import copy
import time



# Action Functions  
#move-up     
def Move_up(node,map_canvas):
    #print(node)
    current_node = copy.deepcopy(node)
    #print(current_node)
    next_node=[current_node[0],current_node[1]-1]
    #print(map_canvas[current_node[0]][current_node[1]-1] )
    
    #node should not be in obstacle space
    if(current_node[1] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and  (map_canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
# move-down
def Move_down(node,map_canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0],current_node[1]+1]
    
    if(next_node[1] < 500) and (map_canvas[next_node[0]][next_node[1]][0]==0) and  (map_canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
#move-right  
def Move_right(node,map_canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]+1,current_node[1]]
    
    if(next_node[0] < 1200) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
#move-left
def Move_left(node,map_canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]-1,current_node[1]]
    
    if(next_node[0] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
#move-right-down (diagonally down   
def move_left_up(node,map_canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]-1,current_node[1]]
    
    if(next_node[1] > 0) and (next_node[0] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None

#move-right-up (diagonally up)
def move_right_up(node,map_canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]-1,current_node[1]]
    
    if(next_node[1] > 0) and (next_node[0] < 1200) and  (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
#move-right-down (diagonally down)
def move_right_down(node,map_canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]-1,current_node[1]]
    
    if(next_node[1] < 500) and (next_node[0] < 1200) and  (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
    
#move-left-down (diagonally down)    
def move_left_down(node,map_canvas):
    
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]-1,current_node[1]]
    
    if(next_node[1] < 500) and (next_node[0] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        return tuple(next_node)
    else:
        return None
