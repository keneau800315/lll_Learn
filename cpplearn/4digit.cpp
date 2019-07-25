#include <iostream>
using namespace std;
int main(){
int num,th,hu,te,un;
	cout<<"enter a number(0-9999): ";
	cin>>num;
	th=num/1000;
	hu=num%1000/100;
	te=num%100/10;
	un=num%10;
	cout<<th<<" "<<hu<<" "<<te<<" "<<un<<endl;
	return 0;
}
