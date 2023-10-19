#include <bits/stdc++.h>
#define int long long

using namespace std;



int32_t main() {
    int n, m;
    cin >> n >> m;
    
    int c[n][m];
    int dp[n][m];
    
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> c[i][j];
            dp[i][j] = 0;
        }
    }

    dp[0][0] = c[0][0];

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i || j) {   
                dp[i][j] = INT_MAX;     

                if (i - 1 >= 0) {
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + c[i][j]);
                }

                if (j - 1 >= 0) {
                    dp[i][j] = min(dp[i][j], dp[i][j - 1] + c[i][j]);
                }
            }
        }
    }

    cout << dp[n - 1][m - 1];
}