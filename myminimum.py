

import math
def minimumCheck(applyList):
    assigned = [-1,-1,-1,1]
    minWage = math.inf
    currentConfig = 0
    worker1change = -1
    worker2change = -1
    worker3change = -1
    worker4change = -1
    picked = [0,0,0,0]
    currentCost = 0

    for j1 in range(len(applyList)):
        for j2 in range(len(applyList)):    
            for j3 in range(len(applyList)):
                for j4 in range(len(applyList)):
                    if ((j1 != j2)and(j1 !=j3)and(j1!=j4)and (j2!=j3)and (j2!=j4)and(j3!=j4)):
                        
                        currentCost = applyList[0][j1] + applyList[1][j2] + applyList[2][j3] + applyList[3][j4]

                        if currentCost < minWage:

                        
                            picked[0] = j1  
                            
                            picked[1] = j2 
                            
                            picked[2] = j3 
                            
                            picked[3] = j4

                            minWage = currentCost 
                        
                        
                        print(j1,"",j2,"",j3,"",j4,"","cost ",currentCost)
                        
    return picked
applyList =[[20,25,22,28],
            [15,18,23,17],
            [19,17,21,24],
            [58,23,24,24]]
print(minimumCheck(applyList))
                       
