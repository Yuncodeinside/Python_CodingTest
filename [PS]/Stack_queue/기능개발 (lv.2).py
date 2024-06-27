from math import ceil

#zip()
#ceil()

def solution(progress, speeds):
    days = [ceil((100-progress)/speeds) for progress , speeds in zip(progress,speeds)]
    
    answer = []
    max = days[0]
    count = 0
    
    for day in days:
        if day > max:
            answer.append(count)
            count = 1
            max = day
        else:
            count+=1
        
    answer.append(count)
    
    return answer


