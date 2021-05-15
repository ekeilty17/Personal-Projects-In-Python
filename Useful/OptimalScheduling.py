#given some overlapping set of tasks with a known durration, 
#we want to find the optimal schedule that 
#allows us to complete as many tasks as possible

def OptimalScheduling(inp):
    I = list(inp)
    tasks = []
    while len(I) != 0:
        #select task with easliest completion date
        min_end = I[0][1]
        min_end_index = 0
        for j in range(1,len(I)):
            if I[j][1] < min_end:
                min_end = I[j][1]
                min_end_index = j
        tasks += [I[min_end_index]]
        del I[min_end_index]
        #now we need to remove any task whose start date
        #is less than the end date of the task we just picked
        #we have to do this while loop bc the index of everything changes
        #whenever something gets deleted
        overlap = True
        while overlap:
            overlap = False
            for j in range(0, len(I)):
                if I[j][0] < min_end:
                    del I[j]
                    overlap = True
                    break
    return tasks


#(start time, end time)
tasks = [(0,4), (2,6), (3,5), (10,11), (4,8)]
print OptimalScheduling(tasks)
