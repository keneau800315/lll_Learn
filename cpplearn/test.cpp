#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
int dir=0;
int main(){
	char i;
	cin>>i;
	switch(i){
		case 'a': dir=0; break;
		case 's': dir=1;break;
		case 'd': dir=2; break;
		default : dir=99; break;
		
	}
	cout<<"dir = "<<dir<<endl;
}
