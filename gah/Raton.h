#pragma once
#include <iostream>//Librerias usadas
using namespace std;
using namespace System;//neamespaces

class Raton {

protected:
	int cuerpoRatonX;//cuerpo de raton en pos X
	int cuerpoRatonY;//cuerpo de ratn en pos Y
	int dx, dy;
public:
	Raton(int x, int y) {//constructor donde le pasamos la posicion en pantalla del raton
		cuerpoRatonX = x;
		cuerpoRatonY = y;
		dx = 0;//y su velocidad
		dy = 0;
	}
	void setCuerpoRatonX(int x) {
		cuerpoRatonX = x;//set de posiciiones en X y Y
	}
	void setCuerpoRatonY(int y) {
		cuerpoRatonX = y;
	}

	void dibujarRaton() {//dibujaos el raton

		Console::SetCursorPosition(cuerpoRatonX, cuerpoRatonY);
		cout << "--(_c'>";

	}
	void limpiarRaton() {//limpiamos el raton

		Console::SetCursorPosition(cuerpoRatonX, cuerpoRatonY);
		cout << "       ";
	}
	void moverRaton(int direccion) {

		//Direccion 0 es ABAJO
		//Direccion 1 es ARRIBA
		//Direccion 2 es Derecha
		//Direccion 3 es Izquierda
		if (direccion == 0) {

			if (cuerpoRatonY - 1 != 0) {
				cuerpoRatonY--;
			}

		}
		if (direccion == 1) {
			if (cuerpoRatonY + 1 != 39) {
				cuerpoRatonY++;
			}
		}
		if (direccion == 2) {
			if (cuerpoRatonX + 1 != 79) {
				cuerpoRatonX++;
			}
		}
		if (direccion == 3) {
			if (cuerpoRatonX - 1 != 0) {
				cuerpoRatonX--;
			}
		}

	}

	int retornarRatonX() {//retornamos su posicion X
		return cuerpoRatonX;
	}
	int retornarRatonY() {//retornamos su posicion en Y
		return cuerpoRatonY;
	}
};
