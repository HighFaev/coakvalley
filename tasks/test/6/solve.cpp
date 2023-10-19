#include <bits/stdc++.h>
#define int long long

using namespace std;

int32_t main()
{
    int t;
		cin >> t;
		while(t--){
			
				int n;
				cin >> n;
				int s[n];
				int f[n];
				for (int i = 0; i < n; ++i) {
					cin >> s[i];
				}
			
				for (int i = 0; i < n; ++i) {
					cin >> f[i];
				}
				int curTime = 0;
				int d[n];
				for (int i = 0; i < n; ++i) {
					curTime = max(curTime, s[i]);
					d[i] = f[i] - curTime;
					curTime = f[i];
				}
				for (auto now: d) {
					cout << now << " ";
				}
				cout << '\n';
			
		}
}