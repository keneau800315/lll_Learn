#include <iostream>
using namespace std;

int main(){
	int month;
	cout<<"請輸入月份"<<endl;
	cin>>month;
	
	//switch can only int、Char 
	switch(month){
		
	//case x:cannt a variable	
	case 4:
	case 6:
	case 9:
	case 11:
		cout<<"30days"<<endl;
	
	case 1:
	case 3:
	case 5:
	case 7:
	case 10:
	case 12:	
		cout<<"31days\n";
		break;
	case 2:
		cout<<"29or28days"<<endl;
		break;
	default:
		cout<<"error input"<<endl; 
	} 
}
