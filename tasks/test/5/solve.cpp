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
			string s;
			cin >> s;
			map<char, int> number_of_chars;
			for(int i = 0; i < n; i++){
				number_of_chars[s[i]]++;
			}
			
			int ans = 0;
			for(int i = 0; i < n; i++){
				if(number_of_chars[s[i]] == 1){
					ans += 2;
				} else {
					ans += 1;
				}
			}

			cout << ans << '\n';
		}
}