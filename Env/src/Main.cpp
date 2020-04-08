#include <iostream>
#include <string>
#include <algorithm>
using namespace std;
#define REP(i,n) for(int i=0;i<n;i++)
#define INF 2000000000

int main(){
    int W,H,N;
    cin >> W >> H >> N;
    int x,y,a;
    int xM,yM,xm,ym;
    xM = W;
    yM = H;
    xm = 0;
    ym = 0;
    REP(i,N) {
        cin >> x >> y >> a;
        switch (a){
            case 1:
                xm = max(xm, x);
                break;
            case 2:
                xM = min(xM, x);
                break;
            case 3:
                ym = max(ym, y);
                break;
            case 4:
                yM = min(yM, y);
                break;
        }
    } 
    cout << max(0, xM-xm)*max(0, yM-ym) << endl;
}