#include <iostream>// LIBRERIAS USADAS
#include <cstdlib>
#include <ctime>
#include <conio.h>
#include "Juego.h"
using namespace std;//NAMESPACES 
using namespace System;
int generarAleatorio(int M, int N) {

	int tam = rand() % (N - M + 1) + M;//GENERAMOS EL NUMERO ALEATORIO
	return tam;
}

int main() {
	srand(time(NULL));//VALORES RAMDOMS
	Console::CursorVisible = false;//HACEMOS QUE EL CURSOR SEA INVISIBLE
	int x = 80, y = 45;//VALORES FINALES DE LA PANTALLA
	Console::SetWindowSize(80, 45);

	int TOTAL_RATONES = generarAleatorio(7, 15);//TOTAL DE RATONES QUE EMPEZARAN EN LA PANTALLA

	AtrapaAlRaton* atrapa = new AtrapaAlRaton(1, 1);//CREAMOS INSTANCIA Y LE PASAMOS LA POSICION INICIAL DEL GATITO

	//=============================================
	clock_t t, ts;//VARAIBLES PARA SABER EL TIEMPO
	int segundos = 0;
	ts = clock() + CLOCKS_PER_SEC;
	//==========================================

	for (int i = 0; i < TOTAL_RATONES; i++) {
		Raton* nuevoRaton = new Raton(generarAleatorio(5, 75), generarAleatorio(5, 30));
		atrapa->agregarRaton(nuevoRaton);

	}//METEMOS LOS RATONES CREADOS y le pasamos una ubicacion en la pantalla

	while (1) {

		//SI PRESIONA UNA TECLA EL GATITO SE MUEVE
		if (kbhit()) {

			char tecla = getch();

			atrapa->borrarGato();
			atrapa->mover(tecla);
			atrapa->dibujarGato();

		}

		//ESTA FUNCION VERIFICARA SI HAY UN RATONCITO CERCA PARA CAZAR
		atrapa->quitarRatoncito();

		if (TOTAL_RATONES / 2 == atrapa->tamRatonera()) {//SI LOS RATONES INICIANTES FUERON 10 / 2 = 5 SERAN LOS RATONES A CAZAR
			cout << "\n\n\t\t[ FELICIDADEEESSSS GANASTE EL JUEGO  !!!!!!!!!]\n\n";
			getch();
			getch();
			getch();
			getch();
			break;
		}

		if ((t = clock()) >= ts)//SABEMOS EL TIEMPO EN PANTALLA
		{
			++segundos;
			ts = t + CLOCKS_PER_SEC;//SI ES PAR EN 2 SIGNIFICA QUE HA PASADO DOS SEGUNDOS, ENTONCES AUMENTA
			if (segundos % 2 == 0 && atrapa->tamRatonera() < 15) {//PERO TIENE UN LIMITE DE 15 RATONCITOS
				Raton* nuevoRaton = new Raton(generarAleatorio(10, 80), generarAleatorio(5, 40));
				atrapa->agregarRaton(nuevoRaton);
			}
		}

		if (atrapa->tamRatonera() > 0) {//SI HAY RATONCITOS EN LA PANTALLA HACE TODAS LAS ACCIONES PARA CONTROLARLOS
			for (int i = 0; i < atrapa->tamRatonera(); i++) {
				Raton* nuevoRaton = new Raton(0, 0);
				nuevoRaton = atrapa->obtenerRaton(i);
				nuevoRaton->limpiarRaton();
				nuevoRaton->moverRaton(generarAleatorio(0, 15));
				nuevoRaton->dibujarRaton();
			}
		}


		if (atrapa->tamRatonera() != 0) {//VALORES QUE SE PONEN EN EL TITULO DE LA CONSOLA .. PARA SABER COMO VAMOS
			//Por si atrapaa Ratones // EN ESTE PROCESO
			Console::Title = segundos.ToString() + " " + atrapa->tamRatonera().ToString() + " | X : ";
			Console::Title += atrapa->retornarCuerpoGatoX().ToString() + " Y : ";
			Console::Title += atrapa->retornarCuerpoGatoY().ToString() + " | META -> " + (TOTAL_RATONES / 2).ToString();
		}
		_sleep(100);//DORMIDMOS LA CONSOLA PARA QUE SEA MAS LENTO
	}


	getch();
	return 0;
}