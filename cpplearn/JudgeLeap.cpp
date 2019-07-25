#include <iostream>
using namespace std;
int main(){
	int year;
	cout<<"enter the year(0-3999): ";
	cin>>year;
	bool bo;
	bo = (year%400==0 || (year%4==0&year%100!=0))?(true):(false);
	cout<<bo<<"bo";

	if(bo == 1){
	cout<<year<<"is a leap year."<<endl;
	}else{
	cout<<year<<"is not a leap year."<<endl;
	}
	
}
