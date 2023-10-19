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
			string s;
			inputfile >> s;
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

			outputfile << ans << '\n';
		}


		inputfile.close();
		outputfile.close();
	}
}