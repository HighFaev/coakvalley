#include <bits/stdc++.h>
#define int long long
using namespace std;

int32_t main(){
	
	srand(time(NULL));
	for(int test_number = 1; test_number <= 30; test_number++){
		ofstream outputFile("gen_input/input" + to_string(test_number) + ".txt");
		
		int n = rand() % (2*test_number*test_number) + 3;
		int k = rand() % (n * (n-1) / 20 + 1) + 1;
		map <pair<int, int>, int> used_pairs;
		vector<pair<pair<int, int>,int>> graph;
		while(graph.size() < k){
			pair<int, int> new_pair = {rand() % n + 1, rand() % n + 1};
			while(new_pair.first == new_pair.second){
				new_pair = {rand() % n + 1, rand() % n + 1};
			}
			if(new_pair.second < new_pair.first){
				swap(new_pair.first, new_pair.second);
			}
			int value = rand() % 100 + 1;
			if(used_pairs[new_pair] == 0){
				graph.emplace_back(make_pair(new_pair, value));
				used_pairs[new_pair] += 1;
			}
		}
		outputFile << n << ' ' << k << '\n';
		for(auto u: graph){
			outputFile << u.first.first << ' ' << u.first.second << ' ' << u.second << '\n';
		}
		pair<int, int> new_pair = {rand() % n + 1, rand() % n + 1};
		outputFile << new_pair.first << ' ' << new_pair.second << '\n';
		cout << "TEST " << test_number << " DONE" << endl;	
	}
}