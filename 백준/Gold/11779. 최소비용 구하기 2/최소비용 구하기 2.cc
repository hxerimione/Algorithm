#include <iostream>
#include <vector>
#include <queue>
#include <cstring> // for memset

using namespace std;

struct Node {
    int target, price;
    vector<int> route;
    Node(){};
    Node(int _target, int _price) : target(_target), price(_price), route(vector<int>()) {};
    Node(int _target, int _price, vector<int> vec) : target(_target), price(_price), route(vec) {};
    bool operator<(const Node &n) const {
        return price > n.price; // 최소 힙을 위해 큰 값이 먼저 오도록
    }
};

const int INF = (int)1e9;
int dist[1001];  // 각 노드까지의 최소 거리
bool visited[1001];
vector<vector<Node>> v;
vector<int> target_route;

int main() {
    int n, m;
    int target_s, target_e;
    int start, end, price;
    
    scanf("%d", &n);
    v.resize(n+1);  // 1-based index를 위해 n+1 크기로 선언
    scanf("%d", &m);
    
    for (int i = 0; i < m; i++) {
        scanf("%d %d %d", &start, &end, &price);
        v[start].push_back(Node(end, price));  // start에서 end로 가는 간선 추가
    }
    
    scanf("%d %d", &target_s, &target_e);
    
    // 거리 배열 초기화
    for (int i = 1; i <= n; i++) dist[i] = INF;
    
    memset(visited, false, sizeof(visited));
    dist[target_s] = 0;
    
    // 다익스트라 알고리즘을 위한 우선순위 큐
    priority_queue<Node> pq;
    pq.push(Node(target_s, 0, {target_s}));  // 시작 노드에서 시작하므로 경로에 자기 자신 포함
    
    while (!pq.empty()) {
        int te = pq.top().target;  // 현재 노드
        int tp = pq.top().price;   // 현재까지의 비용
        vector<int> tmp_v = pq.top().route;  // 현재까지의 경로
        pq.pop();
        
        if (visited[te]) continue;  // 이미 방문한 노드는 무시
        visited[te] = true;  // 방문 처리
        
        // 목표 지점에 도달했으면 경로 저장 후 종료
        if (te == target_e) {
            target_route = tmp_v;
            break;
        }

        // 인접한 노드들에 대해 탐색
        for (Node next : v[te]) {
            if (dist[next.target] > tp + next.price) {
                dist[next.target] = tp + next.price;  // 최소 거리 갱신
                vector<int> new_route = tmp_v;  // 경로 복사
                new_route.push_back(next.target);  // 다음 노드 추가
                pq.push(Node(next.target, dist[next.target], new_route));  // 큐에 넣기
            }
        }
    }
    
    // 최종 비용 출력
    printf("%d\n", dist[target_e]);
    
    // 경로 출력
    printf("%d\n", (int)target_route.size());
    for (int node : target_route) {
        printf("%d ", node);
    }
    printf("\n");
    
    return 0;
}

