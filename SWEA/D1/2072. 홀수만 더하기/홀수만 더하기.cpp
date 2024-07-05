#include <iostream>
using namespace std;
// 3
// 3 17 1 39 8 41 2 32 99 2
// 22 8 5 123 7 2 63 7 3 46
// 6 63 2 3 58 76 21 33 8 1   
int main() {
    int T;
    cin >> T;
    for (int i=0;i<T;i++){
        int numbers[10];//배열 정의
        for (int j=0;j<10;j++){
            cin >> numbers[j];
        }
        int sum=0;
        for (int j=0;j<10;j++){
            if (numbers[j]%2 ==1){
                sum+= numbers[j];
            }
        }
        cout <<"#" <<i+1<<" "<< sum<<endl;
    }
    

    return 0;
}