
#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;
    int max;
    int N;
    for (int tc = 1; tc <= T; tc++) {
        max=0;
        for (int i=0;i<10;i++){
            cin >> N;
            if (N > max){
                max = N;
            }
        }
        // printf("#%d %.1f\n",tc,answer);
        cout << "#" << tc << " " << max << endl;
    }
    
    return 0;
}
