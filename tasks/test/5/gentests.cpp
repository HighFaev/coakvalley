#include <bits/stdc++.h>

using namespace std;

int main(){
	
	srand(time(NULL));
	string input_string_char = "QWERTYUIOPASDFGHJKLZXCVBNM";
	for(int test_number = 1; test_number <= 30; test_number++){
		ofstream outputFile("gen_input/input" + to_string(test_number) + ".txt");
		int t = rand() % 100 + 1;
		outputFile << t << '\n';
		while (t--)
		{
			int n = rand() % 1000 + 1;
			outputFile << n << '\n';
			string input_string = "";
			while(n--){
				int pos = rand() % 26;
				input_string += input_string_char[pos];
			}
			outputFile << input_string << '\n';
		}
			
	}
}