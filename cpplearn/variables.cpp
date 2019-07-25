#include <iostream>
using namespace std;
int golable_var=10;
int a=5;
int main(){
	int local_var =5;
	int a;
	cout<<"please input an int\n";
	cin>>a;
	cout<<"local= "<<local_var<<endl;
	cout<<"golable= "<<golable_var<<endl;
	cout<<"int a="<<a<<endl;
	//::a取全域變數 
	cout<<"golable a"<<::a<<endl;
	return 0;
}
