#include <iostream>
using namespace std;

int main(){
	int num;
	cout<<"enter a positive integer:";
	cin>>num;
	cout<<num<<" ";
	while(num!=1){
	if(num<=0){cout<<num<<" is not a positive integer";
	break;
	}	
	else if(num%2 !=0){
		num =3*num+1;
		}
	else{
		num /=2;
		}
		cout<<num<<" ";
	}
	return 0;
}
