/* myfrist c program
*/


/*
#前處理指令 #include、#define、#ifdef、#ifndef、#endif、、、
代表前處理器要做的動作 

iostream標頭黨(header file) ，iostream(library)類似io參考書定義了很多的詞與用法解釋 

*/

#include <iostream>


// 以後只要出現num 全部使用18去取代 ，不是變數 
#define num 18
// namespace避免同個或不同的標頭檔案出現一樣的某個詞 ，這裡指定使用在std裡的cout 
using namespace std;


// main function程式開始與結束的地方一定要有 
//int 代表函式的輸出(回傳直)型態未integer，main function 一定要int main()， char 小數..都不行 
//main後的括號放參數輸入類型或名稱main()= main(void)
//{}裡面放處理過程 
//字串不用""刮起來電腦會以為字串是物件或變數  
int main(){
	cout<<"Hello world!"<<endl;
	
	//不加 using namespace std，可將改為std::cout <<"Hello world!"<<std::endl;
	cout<<num<<endl;
	//同常回傳0代表程式正確執行 ，return跳出函試不帶任何回傳 
	return 0;
	//return跳脫下面程式不執行 
	cout<<num<<endl;
}


//end of file
