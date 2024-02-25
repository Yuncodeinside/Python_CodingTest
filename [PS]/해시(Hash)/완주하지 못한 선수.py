def solution(participant, completion):
    # 해시를 사용하여 참가자 명단을 기록
    participant_dict = {}
    
    # 참가자 명단에 있는 선수들을 해시에 추가하고, 동명이인이 있으면 값을 증가시킴
    for person in participant:
        if person in participant_dict:
            #동명이인
            participant_dict[person] += 1
            print(participant_dict)
        else:
            #명단에 존재하지 않았음
            participant_dict[person] = 1
    
    # 완주한 선수들을 해시에서 빼서 값을 감소시킴
    for person in completion:
        participant_dict[person] -= 1
    
    # 값이 0이 아닌 선수가 완주하지 못한 선수
    for key, value in participant_dict.items():
        if value != 0:
            return key

# Example usage:
participants = ["leo", "kiki", "eden"]
completions = ["eden", "kiki"]
result = solution(participants, completions)
print(result)
