

#include "arrEclipse.h"
using namespace std;

int menu() {
	int opcion;
	do {
		cout << "\t\tMani PRINCIPAL\n";
		cout << "\t1. Registro de datos\n";
		cout << "\t2. Modificar un dato\n";
		cout << "\t3. Reporte\n";
		cout << "\t4. Eliminar un dato\n";
		cout << "\t5. Reporte de eclipses vistos en Europa\n";
		cout << "\t6. Reporte de eclipses que ocasionar sismos\n";
		cout << "\t7. Reporte de eclipses que se produjeron en la noche\n";
		cout << "\t8. Salir\n";
		cout << "\tIngresar opcion: "; cin >> opcion;
	} while (!(opcion > 0 && opcion < 8));
	return opcion;
}

int main() {
	int posicion;

	string tipo;
	string fecha;
	int hora;
	bool sismos;
	bool lluvias;
	string visibilidad;

	eclipse* objEclipse = nullptr;
	arrEclipse* objArrEclipse = new arrEclipse();

	while (true) {
		system("cls");
		int opcion = menu();
		if (opcion == 7) {
			system("cls");
			break;
		}
		system("cls");

		switch (opcion) {
		case 1:
			cout << "\t\tREGISTRO DE DATOS\n\n";
			cout << "\tTipo de eclipse (solar o lunar): "; cin >> tipo;
			cout << "\tFecha (mes): "; cin >> fecha;
			cout << "\tHora (ej:100 = 1 am.): "; cin >> hora;
			cout << "\tSismos (1: si, 0: no): "; cin >> sismos;
			cout << "\tLluvias (1: si, 0: no): "; cin >> lluvias;
			cout << "\tVisibilidad (America del Sur, Europa, Africa, America del Norte, Asia): "; cin >> visibilidad;

			objArrEclipse->agregarEclipse(new eclipse(tipo, fecha, hora, sismos, lluvias, visibilidad));

			cout << "\tRegistro exitoso...";
			break;
		case 2:
			if (objArrEclipse->getNumeroEclipses() == 0) break;

			cout << "\t\tMODIFICAR CONTACTO\n\n";
			do {
				cout << "\tPosicion: "; cin >> posicion;
			} while (posicion < 0 || posicion >= objArrEclipse->getNumeroEclipses());

			objEclipse = objArrEclipse->getEclipeSegunPosicion(posicion);
			cout << "\t\tREGISTRO DE DATOS\n\n";
			cout << "\tTipo de eclipse (solar o lunar): "; cin >> tipo;
			cout << "\tFecha (mes): "; cin >> fecha;
			cout << "\tHora (ej:100 = 1 am.): "; cin >> hora;
			cout << "\tSismos (1: si, 0: no): "; cin >> sismos;
			cout << "\tLluvias (1: si, 0: no): "; cin >> lluvias;
			cout << "\tVisibilidad (America del Sur, Europa, Africa, America del Norte, Asia): "; cin >> visibilidad;

			objEclipse->setTipo(tipo);
			objEclipse->setFecha(fecha);
			objEclipse->setHora(hora);
			objEclipse->setSismos(sismos);
			objEclipse->setLluvias(lluvias);
			objEclipse->setVisibilidad(visibilidad);
			objEclipse = nullptr;
			break;
		case 3:
			cout << "\t\tLISTA DE ECLIPSES\n\n";
			objArrEclipse->reporte();
			break;
		case 4:
			if (objArrEclipse->getNumeroEclipses() == 0) break;

			cout << "\t\tELIMINAR ECLIPSES\n\n";
			do {
				cout << "\tPosicion (de 0 en adelante): "; cin >> posicion;
				--posicion;
			} while (posicion < 0 || posicion >= objArrEclipse->getNumeroEclipses());
			objArrEclipse->eliminarPlato(posicion);

			cout << "\tContacto eliminado correctamente...";
			break;
		case 5:
			cout << "\t\tREPORTE DE ECLIPSES VISTOS EN EUROPA\n";
			objArrEclipse->reporteEclipsesEuropa();
			break;
		case 6:
			cout << "\t\tREPORTE DE ECLIPSES QUE OCASIONAR SISMOS\n";
			objArrEclipse->reporteEclipsesQueCausaronSismos();
			break;
		case 7:
			cout << "\tREPORTE DE ECLIPSES QUE SE PRODUJERON EN LA NOCHE\n";
			objArrEclipse->reporteEclipsesNoche();
			break;
		}
		system("pause>0");
	}
	delete objArrEclipse;
	return 0;
}
