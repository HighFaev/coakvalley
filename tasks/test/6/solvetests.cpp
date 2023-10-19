#include <bits/stdc++.h>
#define int long long

using namespace std;

int32_t main(){
	
	for(int test_number = 1; test_number <= 30; test_number++){
        string name_of_inputFile = "gen_input/input" + to_string(test_number) + ".txt";
		string name_of_outputFile = "gen_output/output" + to_string(test_number) + ".txt";
		
		ifstream inputfile;
		ofstream outputfile;
		inputfile.open(name_of_inputFile);
		outputfile.open(name_of_outputFile);

		int t;
		inputfile >> t;
		while(t--){
			
				int n;
				inputfile >> n;
				int s[n];
				int f[n];
				for (int i = 0; i < n; ++i) {
					inputfile >> s[i];
				}
			
				for (int i = 0; i < n; ++i) {
					inputfile >> f[i];
				}
				int curTime = 0;
				int d[n];
				for (int i = 0; i < n; ++i) {
					curTime = max(curTime, s[i]);
					d[i] = f[i] - curTime;
					curTime = f[i];
				}
				for (auto now: d) {
					outputfile << now << " ";
				}
				outputfile << '\n';
			
		}
		inputfile.close();
		outputfile.close();
		cout << "TEST " << test_number << " DONE" << endl;	
	}	
}
