#include <bits/stdc++.h>

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
		ans = "False";
		
		int n, k;
		inputfile >> n >> k;

		for(int i = 0; i < k; i++){
			int v1, v2;
			inputfile >> v1 >> v2;
			graph[v1].emplace_back(v2);
		}
		 
		inputfile >> v_start >> v_end;
		used[v_start] = true;
		dfs(v_start);
		outputfile << ans;


		inputfile.close();
		outputfile.close();
		cout << "TEST " << test_number << " DONE" << endl;	
	}	
}
