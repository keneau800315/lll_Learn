#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main(){
	srand(time(NULL));
	int canswer=rand()%100;
	int guess=0;
	int count=0,cell=99,floor=0;
	cout<<canswer<<endl;
	string man;
	while(guess !=canswer){
		count += 1;
		man = (count%2 != 0)?("P1"):("P2");	
		cout<< man << " enter a numer"<<"("<<floor<<"~"<<cell<<")"<<endl;
		cin>>guess;	
		if(guess ==canswer){
			cout<<man<<" Win!"<<endl;
			break;
		}
	else if(guess == -1){
		break;
		}	
		else if(guess < canswer){ 
			cout<<"Too small!"<<endl;
			if(floor<guess)
			floor=guess+1;
			
		}
		
		else{
			cout<<"Too large"<<endl;
			if(guess<cell)
			cell=guess-1;
		
		}		
	
	}

}
