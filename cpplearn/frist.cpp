/* myfrist c program
*/


/*
#�e�B�z���O #include�B#define�B#ifdef�B#ifndef�B#endif�B�B�B
�N��e�B�z���n�����ʧ@ 

iostream���Y��(header file) �Aiostream(library)����io�ѦҮѩw�q�F�ܦh�����P�Ϊk���� 

*/

#include <iostream>


// �H��u�n�X�{num �����ϥ�18�h���N �A���O�ܼ� 
#define num 18
// namespace�קK�P�өΤ��P�����Y�ɮץX�{�@�˪��Y�ӵ� �A�o�̫��w�ϥΦbstd�̪�cout 
using namespace std;


// main function�{���}�l�P�������a��@�w�n�� 
//int �N��禡����X(�^�Ǫ�)���A��integer�Amain function �@�w�nint main()�A char �p��..������ 
//main�᪺�A����Ѽƿ�J�����ΦW��main()= main(void)
//{}�̭���B�z�L�{ 
//�r�ꤣ��""��_�ӹq���|�H���r��O������ܼ�  
int main(){
	cout<<"Hello world!"<<endl;
	
	//���[ using namespace std�A�i�N�אּstd::cout <<"Hello world!"<<std::endl;
	cout<<num<<endl;
	//�P�`�^��0�N��{�����T���� �Areturn���X��դ��a����^�� 
	return 0;
	//return����U���{�������� 
	cout<<num<<endl;
}


//end of file
