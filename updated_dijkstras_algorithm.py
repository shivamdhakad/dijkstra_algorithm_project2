# edited the action function
# diagonal move : action function were not correct in previous code

# import libraries
import cv2
import numpy as np
import heapq as hq
import copy
import time

# Action Functions  
#move-up     
# def Move_up(node,map_canvas):
#     #print(node)
#     current_node = copy.deepcopy(node)
#     #print(current_node)
#     next_node=[current_node[0],current_node[1]-1]
#     #print(map_canvas[current_node[0]][current_node[1]-1] )
#     # check if node is not in obsctacle space
#     if(current_node[1] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and  (map_canvas[next_node[0]][next_node[1]][2]==0):
#         return tuple(next_node)
#     else:
#         return None
    
# # move-down
# def Move_down(node,map_canvas):
#     current_node = copy.deepcopy(node)
#     next_node=[current_node[0],current_node[1]+1]
#     if(next_node[1] < 500) and (map_canvas[next_node[0]][next_node[1]][0]==0) and  (map_canvas[next_node[0]][next_node[1]][2]==0):
#         return tuple(next_node)
#     else:
#         return None
    
# #move-right  
# def Move_right(node,map_canvas):
#     current_node = copy.deepcopy(node)
#     next_node=[current_node[0]+1,current_node[1]]
#     if(next_node[0] < 1200) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
#         return tuple(next_node)
#     else:
#         return None
    
# #move-left
# def Move_left(node,map_canvas):
#     current_node = copy.deepcopy(node)
#     next_node=[current_node[0]-1,current_node[1]]
#     if(next_node[0] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
#         return tuple(next_node)
#     else:
#         return None
    
# #move-right-down (diagonally down   
# def move_left_up(node,map_canvas):
#     current_node = copy.deepcopy(node)
#     # next_node=[current_node[0]-1,current_node[1]]
#     next_node=[current_node[0]-1,current_node[1]-1]
#     if(next_node[1] > 0) and (next_node[0] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
#         return tuple(next_node)
#     else:
#         return None

# #move-right-up (diagonally up)
# def move_right_up(node,map_canvas):
#     current_node = copy.deepcopy(node)
#     # next_node=[current_node[0]-1,current_node[1]]
#     next_node=[current_node[0]+1,current_node[1]-1]

#     if(next_node[1] > 0) and (next_node[0] < 1200) and  (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
#         return tuple(next_node)
#     else:
#         return None
    
# #move-right-down (diagonally down)
# def move_right_down(node,map_canvas):
#     current_node = copy.deepcopy(node)
#     # next_node=[current_node[0]-1,current_node[1]]
#     next_node = [current_node[0]+1,current_node[1]+1]
#     if(next_node[1] < 500) and (next_node[0] < 1200) and  (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
#         return tuple(next_node)
#     else:
#         return None
    
# #move-left-down (diagonally down)    
# def move_left_down(node,map_canvas):
#     current_node = copy.deepcopy(node)
#     # next_node=[current_node[0]-1,current_node[1]]
#     next_node = [current_node[0]-1,current_node[1]+1]    
#     if(next_node[1] < 500) and (next_node[0] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
#         return tuple(next_node)
#     else:
#         return None

def Move_up(node,map_canvas):
    #print(node)
    current_node = copy.deepcopy(node)
    # print("current_node",current_node)
    # next_node=[current_node[0],current_node[1]-1]
    next_node=[current_node[0]-1,current_node[1]]
    # print("up",next_node)
    # check if node is not in obsctacle space
    if(current_node[1] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and  (map_canvas[next_node[0]][next_node[1]][2]==0):
        print("up")
        return tuple(next_node)
    else:
        return None
    
# move-down
def Move_down(node,map_canvas):
    current_node = copy.deepcopy(node)
    next_node=[current_node[0]+1,current_node[1]]
    print("next_node:",next_node)
    # if(next_node[1] < 500) and (map_canvas[next_node[0]][next_node[1]][0]==0) and  (map_canvas[next_node[0]][next_node[1]][2]==0):
    if(next_node[1] < 1200) and (map_canvas[next_node[0]][next_node[1]][0]==0) and  (map_canvas[next_node[0]][next_node[1]][2]==0):
        print("dn")
        return tuple(next_node)
    else:
        print("!dn")
        return None
    
#move-right  
def Move_right(node,map_canvas):
    current_node = copy.deepcopy(node)
    next_node=[current_node[0],current_node[1]+1]
    if(next_node[0] < 1200) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        print("rg")
        return tuple(next_node)
    else:
        return None
    
#move-left
def Move_left(node,map_canvas):
    current_node = copy.deepcopy(node)
    next_node=[current_node[0],current_node[1]-1]
    if(next_node[0] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        print("lf")
        return tuple(next_node)
    else:
        return None
    
#move-left-up (diagonally down   
def move_left_up(node,map_canvas):
    current_node = copy.deepcopy(node)
    # next_node=[current_node[0]-1,current_node[1]]
    next_node=[current_node[0]-1,current_node[1]-1]
    if(next_node[1] > 0) and (next_node[0] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        print("lf-up")
        return tuple(next_node)
    else:
        return None

#move-right-up (diagonally up)
def move_right_up(node,map_canvas):
    current_node = copy.deepcopy(node)
    # next_node=[current_node[0]-1,current_node[1]]
    next_node=[current_node[0]-1,current_node[1]+1]

    if(next_node[1] > 0) and (next_node[0] < 1200) and  (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        print("rg-up")
        return tuple(next_node)
    else:
        return None
    
#move-right-down (diagonally down)
def move_right_down(node,map_canvas):
    current_node = copy.deepcopy(node)
    # next_node=[current_node[0]-1,current_node[1]]
    next_node = [current_node[0]+1,current_node[1]+1]
    print("next_node:",next_node)
    # if(next_node[1] < 500) and (next_node[0] < 1200) and  (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
    if(next_node[1] > 0) and (next_node[0] < 1200) and  (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        print("rg_dn")
        return tuple(next_node)
    else:
        print("!rg-dn")
        return None
    
#move-left-down (diagonally down)    
def move_left_down(node,map_canvas):
    current_node = copy.deepcopy(node)
    # next_node=[current_node[0]-1,current_node[1]]
    next_node = [current_node[0]+1,current_node[1]-1]    
    print("next_node:",next_node)
    # if(next_node[1] < 500) and (next_node[0] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
    if(next_node[1] > 0) and (next_node[0] > 0) and (map_canvas[next_node[0]][next_node[1]][0]==0) and (map_canvas[next_node[0]][next_node[1]][2]==0):
        print("lf-dn")
        return tuple(next_node)
    else:
        print("!lf-dn")
        return None

#Dijkstra Algorithm
def Dijkstra(start_node, goal_node,map_canvas):

    S={}
    PQ=[]
    temp=0
    hq.heapify(PQ)
    hq.heappush(PQ,[0,start_node,start_node])   #PQ= priority Queue. Elements: cost,parent,present
    while(len(PQ)!=0):
        node=hq.heappop(PQ)
        # print("poped_node:",node)
        S[(node[2][0],node[2][1])]=node[1]
        present_cost=node[0]
        if(list(node[2])==goal_node):
            print("path generating...")
            # calling back tracking function
            Backtrack(S,start_node,goal_node,map_canvas)
            temp=1
            break
        
        # action sequence to explore next_node   
        # next_node=Move_up(node[2],map_canvas)     
        # next_node1=move_right_up(node[2],map_canvas)
        # next_node2=Move_right(node[2],map_canvas)
        # next_node3=move_right_down(node[2],map_canvas)         
        # next_node4=Move_down(node[2],map_canvas)
        # next_node5=move_left_down(node[2],map_canvas)
        # next_node6=Move_left(node[2],map_canvas)
        # next_node7=move_left_up(node[2],map_canvas) 

        #given action sequence
        next_node=Move_up(node[2],map_canvas)
        #print(next_node)                 
        next_node1=Move_down(node[2],map_canvas)
        next_node2=Move_left(node[2],map_canvas)
        next_node3=Move_right(node[2],map_canvas)
        next_node4=move_left_up(node[2],map_canvas)
        next_node5=move_right_up(node[2],map_canvas)
        next_node6=move_left_down(node[2],map_canvas)
        next_node7=move_right_down(node[2],map_canvas)
        
  
        
        if(next_node):
          
            if(next_node not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node[0],next_node[1]]):
                        flag=1
                        #print(i)
                        if(PQ[i][0]>(present_cost+1)):
                            PQ[i][0]=present_cost+1
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break   #breaks for- no point in continuing after finding the index
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1,node[2],[next_node[0],next_node[1]]])
                    hq.heapify(PQ)
                    
                    
        if(next_node1):
            
            if(next_node1 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node1[0],next_node1[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1):
                            PQ[i][0]=present_cost+1
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1,node[2],[next_node1[0],next_node1[1]]])
                    hq.heapify(PQ)
                    
                    
        if(next_node2):
            
            if(next_node2 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node2[0],next_node2[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1):
                            PQ[i][0]=present_cost+1
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1,node[2],[next_node2[0],next_node2[1]]])
                    hq.heapify(PQ)
                          
        
        if(next_node3):
            
            if(next_node3 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node3[0],next_node3[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1):
                            PQ[i][0]=present_cost+1
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1,node[2],[next_node3[0],next_node3[1]]])
                    hq.heapify(PQ)
                    
        
        if(next_node4):
            
            if(next_node4 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node4[0],next_node4[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1.4):
                            PQ[i][0]=present_cost+1.4
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1.4,node[2],[next_node4[0],next_node4[1]]])
                    hq.heapify(PQ)
                    
                    
        if(next_node5):
            
            if(next_node5 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node5[0],next_node5[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1.4):
                            PQ[i][0]=present_cost+1.4
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1.4,node[2],[next_node5[0],next_node5[1]]])
                    hq.heapify(PQ)
                    

        if(next_node6):
            
            if(next_node6 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node6[0],next_node6[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1.4):
                            PQ[i][0]=present_cost+1.4
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1.4,node[2],[next_node6[0],next_node6[1]]])
                    hq.heapify(PQ)
                    
        
        if(next_node7):
            
            if(next_node7 not in S):
                flag=0
                for i in range(len(PQ)):
                    if(PQ[i][2]==[next_node7[0],next_node7[1]]):
                        flag=1
                        if(PQ[i][0]>present_cost+1.4):
                            PQ[i][0]=present_cost+1.4
                            PQ[i][1]=node[2]
                            hq.heapify(PQ)
                        break
                if(flag==0):
                    hq.heappush(PQ,[present_cost+1.4,node[2],[next_node7[0],next_node7[1]]])
                    hq.heapify(PQ)
    # if no node is generated, then goal is not reachable 
    if temp==0 :
        print("Goal cannot be reached")


#backtracking function, takes parent node from explored nodes and stores the coordinates of the path in a new list
def Backtrack(S,start_node,goal_node,map_canvas):
    count =0
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # write the video file in mp4 format
    frame_rate = 500   # frame rate
    out = cv2.VideoWriter('dijkstra_explore_path.mp4',fourcc,frame_rate,(map_canvas.shape[1],map_canvas.shape[0]))
    explored_nodes=S.keys()
    navigation=[]
    navigation.append(goal_node)
    start=copy.deepcopy(start_node)
    goal=copy.deepcopy(goal_node)
    start.reverse()
    goal.reverse()
    cv2.circle(map_canvas,tuple(start),3,(0,255,0),-1)           #draw green and red circles representing the start & goal
    cv2.circle(map_canvas,tuple(goal),3,(0,0,255),-1)
    for node in explored_nodes:
        count = count +1
        map_canvas[node[0]][node[1]]=[255,255,255]
        if count % 100 == 0: 
            cv2.imshow("Nodes Exploration",map_canvas)
            cv2.waitKey(1)
            out.write(map_canvas)
    parent=S[tuple(goal_node)]
    while(parent!=start_node):
        navigation.append(parent)
        parent=S[tuple(parent)]
    navigation.append(start_node)
    
    # draw the path on the map_canvas
    while(len(navigation)>0):
        path_node = navigation.pop()
        map_canvas[path_node[0]][path_node[1]] =[255, 0, 0]    # blue color path_line
        out.write(map_canvas)
    # #####EDITED_PART #####
    # while(len(navigation)>0):
    #     path_node = navigation.pop()
    #     map_canvas[path_node[0]][path_node[1]] =[255, 0, 0]
    # out.write(map_canvas)
    # #########################
    
    cv2.imshow("Nodes Exploration",map_canvas)
    out.release()
    print(navigation)
    

if __name__ == '__main__':
    start_time = time.time()
    start=[]
    goal=[]
    #create a map of 500x1200
    map_canvas = np.zeros((500, 1200, 3), dtype='uint8')

# calculate the vertices of the hexagon
    robot_clearance= 5
    clearance_color=(140,240,140)

    center_x = 650   # hexagon center
    center_y = 250

    vertices = [] # list to store the vertices of the hexagon
    vertices_clearance=[]
    # hexacgon vertices radius
    radius = 150
    clearance_radius= 155
    #calculate the vertices of the hexagon
    for i in range(6):
        x = center_x + radius * np.cos(i * np.pi / 3)
        y = center_y + radius * np.sin(i * np.pi / 3)
        vertices.append((int(x), int(y)))
    
    for i in range(6):
        x = center_x + clearance_radius * np.cos(i * np.pi / 3)
        y = center_y + clearance_radius * np.sin(i * np.pi / 3)
        vertices_clearance.append((int(x), int(y)))

# draw the hexagon on the map_canvas
    cv2.fillPoly(map_canvas,[np.array(vertices_clearance)], clearance_color)
    cv2.fillPoly(map_canvas, [np.array(vertices)], (255,0,0))


# show the map_canvas
    M = cv2.getRotationMatrix2D((center_x, center_y), 90, 1.0)
    map_canvas = cv2.warpAffine(map_canvas, M, (map_canvas.shape[1], map_canvas.shape[0]))

    #rectangle coordinates
    rectangle1=[[100,0],[175,0],[175,400],[100,400]]
    rect1_clearance=[[95,0],[180,0],[180,405],[95,405]]

    rectangle2=[[275,100],[350,100],[350,500],[275,500]]
    rect2_clearance=[[270,95],[355,95],[355,500],[270,500]]
    
    rectangle3=[[900,50],[1100,50],[1100,125],[900,125]]
    rect3_clearance=[[895,45],[1105,45],[1105,130],[895,130]]

    rectangle4=[[900,375],[1100,375],[1100,450],[900,450]]
    rect4_clearance=[[895,370],[1105,370],[1105,455],[895,455]]

    rectangle5=[[1020,120],[1100,120],[1100,380],[1020,380]]
    rect5_clearance=[[1015,120],[1105,120],[1105,380],[1015,380]]

    vertices1=np.array(rectangle1,dtype=np.int32)
    vertices2=np.array(rectangle2,dtype=np.int32)
    vertices3=np.array(rectangle3,dtype=np.int32)
    vertices4=np.array(rectangle4,dtype=np.int32)
    vertices5=np.array(rectangle5,dtype=np.int32)
    # draw the rectangle on the map_canvas using fillPoly
    cv2.rectangle(map_canvas, (0, 0), (map_canvas.shape[1] - 1, map_canvas.shape[0] - 1), clearance_color, robot_clearance)
    cv2.fillPoly(map_canvas, [np.array(rect1_clearance)], clearance_color)
    cv2.fillPoly(map_canvas, [np.array(rect2_clearance)], clearance_color)
    cv2.fillPoly(map_canvas, [np.array(rect3_clearance)], clearance_color)
    cv2.fillPoly(map_canvas, [np.array(rect4_clearance)], clearance_color)
    cv2.fillPoly(map_canvas, [np.array(rect5_clearance)], clearance_color)

    cv2.fillPoly(map_canvas, [np.array(vertices1)], (255,0,0))
    cv2.fillPoly(map_canvas, [np.array(vertices2)], (255,0,0))
    cv2.fillPoly(map_canvas, [np.array(vertices3)], (255,0,0))
    cv2.fillPoly(map_canvas, [np.array(vertices4)], (255,0,0))
    cv2.fillPoly(map_canvas, [np.array(vertices5)], (255,0,0))
   
  
    while(1):
        # take the start and goal coordinates from the user
        print("path planning using Dijkstra Algorithm")
        x1=input( "Enter start position coordinates(x): ")
        y1=input( "Enter start position coordinates(y): ")
        start.append(500-int(y1))
        start.append(int(x1))
        print("start",start)
        x2=input( "Enter goal position coordinates(x): ")        
        y2=input( "Enter goal position coordinates(y): ")
        goal.append(500-int(y2))
        goal.append(int(x2))
        print("goal",goal)
        # check of inbound conditions for the start and goal nodes
        if(int(x1) > 1200 or int(y1)>500 or int(x2) > 1200 or int(y2)>500):
            print("enter the coordinates within the map space(1200,500)")
            
        elif map_canvas[int(y2)][int(x2)][0]!=0 or map_canvas[int(y2)][int(x2)][1]!=0 or map_canvas[int(y2)][int(x2)][2]!=0:
            print("Goal in obstacle space,  try again")
            
        elif map_canvas[int(y1)][int(x1)][0]!=0 or map_canvas[int(y1)][int(x1)][1]!=0 or map_canvas[int(y1)][int(x1)][2]!=0:
            print("Start node in obstacle space, try again")
                       
        else:
            break

        
    # Find the path using Dijkstra Algorithm
    Dijkstra(start,goal,map_canvas)
    end = time.time()
    #print the execution time
    print("Total execution time in seconds: ", int(end - start_time))

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    
