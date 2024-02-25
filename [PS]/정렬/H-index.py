def solution(citations):
    citations.sort(reversed=True)
    
    h_index = max([min(i+1,c) for i,c in enumerate(citations)])
    
    return h_index