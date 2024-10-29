#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    queue<int> bridge; // 다리 위 트럭의 상태를 저장하는 큐
    int current_weight = 0; // 다리 위에 있는 트럭의 현재 무게
    int time = 0; // 경과 시간
    int index = 0; // 대기 중인 트럭의 인덱스

    // 다리 길이만큼 0을 미리 채워놓는다 (트럭이 없음을 의미)
    for (int i = 0; i < bridge_length; i++) {
        bridge.push(0);
    }

    while (!bridge.empty()) {
        time++; // 시간 증가
        current_weight -= bridge.front(); // 다리의 맨 앞 트럭이 나가면 무게에서 제외
        bridge.pop(); // 맨 앞 트럭 제거

        if (index < truck_weights.size()) {
            // 다리가 버틸 수 있는 무게를 넘지 않는다면 트럭을 다리에 올린다.
            if (current_weight + truck_weights[index] <= weight) {
                bridge.push(truck_weights[index]); // 트럭 다리에 올리기
                current_weight += truck_weights[index]; // 현재 무게 증가
                index++; // 다음 트럭 대기열로 이동
            } else {
                bridge.push(0); // 트럭을 올릴 수 없다면 다리는 그대로 비워둠
            }
        }
    }

    return time;
}

int main() {
    cout << solution(2, 10, {7, 4, 5, 6}) << endl; // 8
    cout << solution(100, 100, {10}) << endl; // 101
    cout << solution(100, 100, {10, 10, 10, 10, 10, 10, 10, 10, 10, 10}) << endl; // 110
    return 0;
}
