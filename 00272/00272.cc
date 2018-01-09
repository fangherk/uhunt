#include <iostream>
#include <typeinfo>
#include <string>
using namespace std;

int main(){

    // read in the line as a string
    string line;
    int count = 0;

    // loop until we have more lines
    // modify the line as a string in place
    // replace one character double quotes
    // with two apostrophes or two single quotes
    // depending on the parity of the count
    while(getline(cin, line)){
        for(int i=0; i<line.size(); i++){
            if(line[i] == '\"'){
                if(count % 2 == 0){
                    line.erase(i,1);
                    line.insert(i, "``");
                }else{
                    line.erase(i,1);
                    line.insert(i, "''");
                }
                count += 1;
            }
        }
        cout << line << endl;
    }
    return 0;
}
