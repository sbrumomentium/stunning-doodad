#pragma once
#include <iostream>//Librerias 
#include <stdio.h>
using namespace std;// namespaces
using namespace System;

class Gato {//La clase Gato

protected:
	int cuerpoGatoX, cuerpoGatoY; // Cuerpo de Gato
	int dx, dy;// velocidda del gato
public:
	Gato(int cuerpoX, int cuerpoY) {//iniciamos donde aparecera el gato
		this->cuerpoGatoX = cuerpoX;//metelos los valores del constructor a las variables
		this->cuerpoGatoY = cuerpoY;
		dx = 0;//inicializamos en 0
		dy = 0;
	}

	int retornarCuerpoGatoX() {
		return cuerpoGatoX;//retornamos cuerpo de gato en posX
	}
	int retornarCuerpoGatoY() {
		return cuerpoGatoY;//retornamos cuerpo de gato en posY
	}
	void dibujarGato() {//dibujamos segun el lado de la pantalla

		Console::SetCursorPosition(cuerpoGatoX, cuerpoGatoY);
		//printf(" /\\_/\\");
		cout << " /\\_/\\";

		Console::SetCursorPosition(cuerpoGatoX, cuerpoGatoY + 1);
		cout << "( o.o )";

		Console::SetCursorPosition(cuerpoGatoX + 1, cuerpoGatoY + 2);
		cout << " >^<";
	}

	void borrarGato() {//borramos el gato.. osea el espacio utilizado le ponemos en blanco

		Console::SetCursorPosition(cuerpoGatoX, cuerpoGatoY);
		printf("      ");
		Console::SetCursorPosition(cuerpoGatoX, cuerpoGatoY + 1);
		cout << "       ";
		Console::SetCursorPosition(cuerpoGatoX + 1, cuerpoGatoY + 2);
		cout << "    ";
	}
	void mover(char direccion)//dependiendo la tecla, avanzara segun la direccion
	{
		//los if dentro del if son para los limites de la pantalla, osea que no se salga
		if (direccion == 'w') {

			if (cuerpoGatoY - 1 != 0) {
				cuerpoGatoY--;
			}

		}
		if (direccion == 's') {
			if (cuerpoGatoY + 1 != 39) {
				cuerpoGatoY++;
			}
		}
		if (direccion == 'd') {
			if (cuerpoGatoX + 1 != 79) {
				cuerpoGatoX++;
			}
		}
		if (direccion == 'a') {
			if (cuerpoGatoX - 1 != 0) {
				cuerpoGatoX--;
			}
		}
	}

};
