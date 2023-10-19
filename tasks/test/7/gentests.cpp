#include <bits/stdc++.h>

using namespace std;

int main(){
	
	srand(time(NULL));
	for(int test_number = 1; test_number <= 30; test_number++){
		ofstream outputFile("gen_input/input" + to_string(test_number) + ".txt");
		
		int n = min(rand() % (30 * test_number) + 1, 500);
		int m = min(rand() % (30 * test_number) + 1, 500); 
		outputFile << n << ' ' << m << '\n';
		for(int i = 0; i < n; i++){
			for(int j = 0; j < m; j++){
				int type = rand() % 3;
				int k = min(rand() % 1000 + 1, 1000);
				if(type == 2){
					k *= -1;
				}
				outputFile << k;
				if(j != m - 1){
					outputFile << ' ';
				}
			}
			if(i != n - 1){
				outputFile << '\n';
			}
		}

		cout << "TEST " << test_number << " DONE" << endl;	
	}
}