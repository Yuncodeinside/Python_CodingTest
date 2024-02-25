def solution(nums):
    #홍박사가 가져가도 된다고 말한 포켓몬의 개수
    num = len(nums)//2
    
    #가장 많은 종류의 포켓몬을 선택하는 방법
    #set 중복을 허용하지 않음
    max = len(set(nums))
    
    return min(num,max)

def solution2(nums):
    max_possible = len(nums) // 2
    unique_pokemons = len(set(nums))
    
    # 선택 가능한 폰켓몬의 개수와 중복을 제거한 폰켓몬 종류의 개수 중 최솟값을 반환
    return min(max_possible, min(nums.count(pokemon) for pokemon in set(nums)))
