#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>

using namespace std;

int main(){
  int n, p;
  int count = 0;

  cin >> n >> p;
  cin.ignore(100,'\n');
  
  while(n !=0 && p !=0){
    count +=1;
    
    for(int i = 0; i < n; ++i){
      string line;
      getline(cin, line);
      // cout << line << endl;
    }
u
    string finalWord;
    double finalPrice = 0 ;
    int finalReq = 0 ;
      
    for(int i =0; i < p; ++i){
      string curr;
      double currPrice;
      int currReq;

      getline(cin, curr);
      // cout << curr;
      cin >> currPrice >> currReq;
      // cout << currPrice << currReq << endl;
      cin.ignore(100, '\n');
      // cout << curr << currPrice << currReq << endl;
      if(currReq > finalReq){
        
        finalPrice = currPrice;
        finalReq = currReq;
        finalWord = curr;
        
      }else if (currReq ==finalReq){
        if(currPrice < finalPrice){
          
          finalPrice = currPrice;
          finalReq = currReq;
          finalWord = curr;
          
        }
      }
    
      for(int i =0; i < currReq; ++i){
        string line;
        getline(cin, line);
        // cout << line << endl;
      }
      // cout << "stop?" <<endl;
    }
    
    cout << "RFP #" << count << endl;

    cin >> n >> p;

    if(n == 0 && p == 0){
      cout << finalWord << endl;
    }else{
      cout << finalWord << "\n" << endl;
    }
   
    cin.ignore(100, '\n');
  }
  return 0;
  
  }
