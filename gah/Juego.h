#pragma once
#include "ArregloRatone.h"//Librerias
#include "Gato.h";//Gatito



class AtrapaAlRaton : public Gato, public Ratonera {//Creando clase con herencia aplicada

public://atrapamos al raton -> constructor de nuestra clase -> luego de gato -> luego de ratonera
	AtrapaAlRaton(int x, int y) : Gato(x, y), Ratonera() {

	}



	void quitarRatoncito() {// Quitando el ratoncito

		for (int i = 0; i < arreglo.size(); i++) {//vamos desde el inicio del vector hast el ultimp

			int _raX = arreglo.at(i)->retornarRatonX();//Obtenemos la posicion del raton en X
			int _raY = arreglo.at(i)->retornarRatonY();//lo mismo pero en y
			//Si el gato esta dentro de estos limites, entonces significa que pudo cazar al ratoncito
			if ((cuerpoGatoX == _raX || cuerpoGatoX == _raX + 1 == cuerpoGatoX == _raX - 1 || cuerpoGatoX == _raX + 2 || cuerpoGatoX == _raX - 2 || cuerpoGatoX == _raX + 3 == cuerpoGatoX == _raX - 3 || cuerpoGatoX == _raX + 4 || cuerpoGatoX == _raX - 4) == true &&
				(cuerpoGatoY == _raY || cuerpoGatoY == _raY + 1 == cuerpoGatoY == _raY - 1 || cuerpoGatoY == _raY + 2 || cuerpoGatoY == _raY - 2 || cuerpoGatoY == _raY + 3 || cuerpoGatoY == _raY - 3 || cuerpoGatoY == _raX + 4 || cuerpoGatoY == _raX - 4) == true) {
				//pasamos a limpiar el espacio usado en la consola del raton
				arreglo.at(i)->limpiarRaton();
				arreglo.at(i)->setCuerpoRatonX(0);//seteamos la posiciona 0a Y
				arreglo.at(i)->setCuerpoRatonY(0);//seteamos la posicion en 0 a Y
				arreglo.at(i)->limpiarRaton();//Limpiamos una ultima vez el raton
				arreglo.erase(arreglo.begin() + i);//eliminamos el ratoncito del arreglo.
				Console::Title = "Lo Cazaste";//imprimimos un titulo pequeno en la parte de arriba de la consola
			}


		}
	}


};
