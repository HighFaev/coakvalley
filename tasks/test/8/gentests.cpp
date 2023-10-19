#include <bits/stdc++.h>

using namespace std;

int main(){
	
	srand(time(NULL));
	for(int test_number = 1; test_number <= 30; test_number++){
		ofstream outputFile("gen_input/input" + to_string(test_number) + ".txt");
		
		int n = rand() % (2*test_number*test_number) + 1;
		int k = rand() % max(n * (n-1) / 6, 1) + 1;
		map <pair<int, int>, int> used_pairs;
		vector<pair<int,int>> graph;
		while(graph.size() < k){
			pair<int, int> new_pair = {rand() % n + 1, rand() % n + 1};
			if(used_pairs[new_pair] == 0){
				graph.emplace_back(new_pair);
				used_pairs[new_pair] += 1;
			}
		}
		outputFile << n << ' ' << k << '\n';
		for(auto u: graph){
			outputFile << u.first << ' ' << u.second << '\n';
		}
		pair<int, int> new_pair = {rand() % n + 1, rand() % n + 1};
		outputFile << new_pair.first << ' ' << new_pair.second << '\n';
		cout << "TEST " << test_number << " DONE" << endl;	
	}
}