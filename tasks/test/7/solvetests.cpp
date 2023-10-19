#include <bits/stdc++.h>

using namespace std;

int32_t main(){
	
	for(int test_number = 1; test_number <= 30; test_number++){
        string name_of_inputFile = "gen_input/input" + to_string(test_number) + ".txt";
		string name_of_outputFile = "gen_output/output" + to_string(test_number) + ".txt";
		
		ifstream inputfile;
		ofstream outputfile;
		inputfile.open(name_of_inputFile);
		outputfile.open(name_of_outputFile);

		int n, m;
		inputfile >> n >> m;
		
		cout << n << ' ' << m << endl;
		int c[n][m];
		int dp[n][m];
		
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				inputfile >> c[i][j];
				dp[i][j] = 0;
			}
		}

		dp[0][0] = c[0][0];

		for (int i = 0; i < n; i++) {
			for (int j = 0; j < m; j++) {
				if (i || j) {   //цикл не должен заходить в клетку (0, 0)
					dp[i][j] = INT_MAX;     //код рассчёта максимума получился
											//достаточно длинным из-за дополнительных
											//проверок на выход за границы матрицы

					if (i - 1 >= 0) {
						dp[i][j] = min(dp[i][j], dp[i - 1][j] + c[i][j]);
					}

					if (j - 1 >= 0) {
						dp[i][j] = min(dp[i][j], dp[i][j - 1] + c[i][j]);
					}
				}
			}
		}

		outputfile << dp[n - 1][m - 1];

		inputfile.close();
		outputfile.close();
		cout << "TEST " << test_number << " DONE" << endl;	
	}	
}
