#pragma once
#include "Raton.h"
#include <iostream>//Librerias usadas
#include <vector>
using namespace std;
using namespace System;//namespaces

class Ratonera {//ratonera donde tenemos el vector de ratones

protected:
	vector<Raton*>arreglo;//creamos el vector del raton
public:
	Ratonera() {//ratonera puesta
		arreglo = vector<Raton*>();//donde iniciamos en 0 ratones
	}
	void agregarRaton(Raton* nuevoRaton) {
		arreglo.push_back(nuevoRaton);//metemos un raton
	}
	Raton* obtenerRaton(int indice) {
		return arreglo.at(indice);//nos retorna el raton edpendiendo su indice
	}
	int tamRatonera() {
		return arreglo.size();//tamanio de la ratonera
	}
	vector<Raton*> retornar() {
		return arreglo;//devolvemos la ratonera declarada en la linea 11.
	}
};
