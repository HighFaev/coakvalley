#include <bits/stdc++.h>
#define int long long
using namespace std;

vector<int> graph[10001];

int v_start, v_end;
string ans = "False";
map<int, bool> used;

bool dfs(int v){
	if(v == v_end){
		ans = "True";
	} else {
		for(int i = 0; i < graph[v].size(); i++){
			if(used[graph[v][i]] == false){
				used[graph[v][i]] = true;
				dfs(graph[v][i]);
			}
				
		}
	}
}

int32_t main(){
	int n, k;
	cin >> n >> k;

	for(int i = 0; i < k; i++){
		int v1, v2;
		cin >> v1 >> v2;
		graph[v1].emplace_back(v2);
	}
		 
	cin >> v_start >> v_end;
	used[v_start] = true;
	dfs(v_start);
	cout << ans;
}