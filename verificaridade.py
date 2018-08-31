#include <iostream>
#include <locale.h> //importar a livraria que permite mudar o idioma

   

using namespace std;
int main(){
	setlocale(LC_ALL, "Portuguese"); //Comando da livraria importada para mudar o idioma
	char Nome[20];
	int Idade;
	bool valid;
	cout << "Insira seu nome" << endl;
	cin >> Nome;
	while (!valid){//impedir q insira letra na idade
		valid = true;
		cout << "Insira sua idade" << endl;
		cin >> Idade;
		if(cin.fail()){
			cin.clear();
			cin.ignore();
			valid = false;
		}
	}
	if(Idade > 30){
		cout << "Acima de 30 anos" << endl;
	} //se não for cumprida, passa para a condição de baixo
	else if(Idade > 20){
		cout << "Acima de 20 anos" << endl;
	}
	else if(Idade > 10){
		cout << "Acima de 10 anos" << endl;
	}
	else{
		cout << "Xô criança";
	}
	return 0;
}
