#include <bits/stdc++.h>
#define int long long

using namespace std;

vector<pair<int, int>> graph[10001];
int ans[10000];

int v_start, v_end;
int minus_one = -1;
map<int, bool> used;

void dfs(int v){
	if(v == v_end){
		minus_one = 0;
	} else {
		for(int i = 0; i < graph[v].size(); i++){
			if(used[graph[v][i].first] == false){
				used[graph[v][i].first] = true;
				dfs(graph[v][i].first);
			}
				
		}
	}
}

int32_t main(){
	
	for(int test_number = 1; test_number <= 30; test_number++){
        string name_of_inputFile = "gen_input/input" + to_string(test_number) + ".txt";
		string name_of_outputFile = "gen_output/output" + to_string(test_number) + ".txt";
		
		ifstream inputfile;
		ofstream outputfile;
		inputfile.open(name_of_inputFile);
		outputfile.open(name_of_outputFile);

		used.clear();
		for(int i = 0; i < 10001; i++){
			graph[i].clear();
		}
		
		int n, k;
		inputfile >> n >> k;

		for(int i = 0; i < k; i++){
			int v1, v2, value;
			inputfile >> v1 >> v2 >> value;
			graph[v1].emplace_back(make_pair(v2, value));
			graph[v2].emplace_back(make_pair(v1, value));
		}
		 
		inputfile >> v_start >> v_end;
		used[v_start] = true;
		dfs(v_start);

		if(minus_one == -1){
			outputfile << -1;
			inputfile.close();
			outputfile.close();
		}

		for (int i = 0; i < 10000; i++) {
        	ans[i] = 1000000000;
    	}

		ans[v_start] = 0;
		priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> q;

		q.push({0, v_start});

		while (!q.empty()) {
			pair<int, int> c = q.top();
			q.pop();

			int dst = c.first, v = c.second;

			if (ans[v] < dst) {
				continue;
			}

			for (pair<int, int> e: graph[v]) {
				int u = e.first, len_vu = e.second;

				int n_dst = dst + len_vu;
				if (n_dst < ans[u]) {
					ans[u] = n_dst;
					q.push({n_dst, u});
				}
			}
    	}

		outputfile << ans[v_end];

		minus_one = -1;
		inputfile.close();
		outputfile.close();
		cout << "TEST " << test_number << " DONE" << endl;	
	}	
}
