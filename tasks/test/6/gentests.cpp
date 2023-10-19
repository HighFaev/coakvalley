#include <bits/stdc++.h>

using namespace std;

int main(){
	
	srand(time(NULL));
	for(int test_number = 1; test_number <= 30; test_number++){
		ofstream outputFile("gen_input/input" + to_string(test_number) + ".txt");
		
		int t = rand() % 1000 + 1;
		outputFile << t << '\n';
		vector<int> n_array(t);

		 		
		while(true){
			int max_sum_n = 100;
			int sum = 0;
			for(int i = 0; i < t; i++){
				n_array[i] = rand() % (max_sum_n) + 1;
				sum += n_array[i];
				max_sum_n -= n_array[i];
				if(sum == 100 && i != t-1){
					sum = 0;
					max_sum_n = 100;
					n_array.clear();
				}
			}
			if(sum <= 10){
				break;
			}
		}
		
		int k = 0;
		while (t--)
		{
			int n = n_array[k]; k++;
			outputFile << n << '\n';
			vector<int> S(n);
			vector<int> F(n);
			map<int, int> used_for_S;
			for(int i = 0; i < n; i++){
				int x = rand() % 100000;
				while(used_for_S[x] != 0){
					x = rand() % 100000;
				}
				used_for_S[x]++;
				S[i] = x;
			}
			sort(S.begin(), S.end());
			used_for_S.clear();

			for(int i = 0; i < n; i++){
				int x = rand() % 100000 + 1;
				while(x < S[i] || (i != 0 && x < F[i - 1])){
					x = (rand() % (100000 + 10*i)) + 1;
				}
				F[i] = x;
				outputFile << S[i];
				if(i != n - 1)
					outputFile << ' ';
			}
			outputFile << '\n';
			for(int i = 0; i < n; i++){
				outputFile << F[i];
				if(i != n - 1)
					outputFile << ' ';
			}
			outputFile << '\n';
		}
		cout << "TEST " << test_number << " DONE" << endl;	
	}
}