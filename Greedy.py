w = [2, 10, 5 ,5]
v = [20, 50, 30, 10]
W = 16
picked = [0,0,0,0]
RemainingCapacity = W
currentValue = 0
currentWeight = 0
currentVperW = 0
maxValue = 0
greedy = 0


greedy =[[2,20,0,1],
        [10,50,0,2],
        [5,30,0,3],
        [5,10,0,4]]
for row in greedy:
    row[2]=row[1]/row[0]    
    #print(row)
#sorted(greedy,key=lambda x: greedy[2])
greedy.sort(key = lambda x: x[2],reverse = True)
print(greedy)
RemainingCapacity = W
n = 0
sum = 0
for row in greedy:
    if row[0] <= RemainingCapacity:
        picked[n] = row[3]
        k += 1
        RemainingCapacity -= row[0]
        sum += row[1]

print(picked," ",sum)
