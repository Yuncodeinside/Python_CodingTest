def solution(my_string, n):
    
    new = ''
    
    for char in my_string:
        new += char*n
    
    return new