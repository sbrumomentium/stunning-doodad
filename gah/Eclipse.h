#pragma once
#include <iostream>
#include <string>
using namespace std;

class eclipse {
private:
	string tipo;
	string fecha;
	int hora;
	bool sismos;
	bool lluvias;
	string visibilidad;

public:
	eclipse(string tipo, string fecha, int hora, bool sismos, bool lluvias, string visibilidad);
	~eclipse();

	string getTipo();
	string getFecha();
	int getHora();
	bool getSismos();
	bool getLluvias();
	string getVisibilidad();

	void setTipo(string tipo);
	void setFecha(string fecha);
	void setHora(int hora);
	void setSismos(bool sismos);
	void setLluvias(bool lluvias);
	void setVisibilidad(string visibilidad);

	void toString();
};

eclipse::eclipse(string tipo, string fecha, int hora, bool sismos, bool lluvias, string visibilidad) {
	this->tipo = tipo;
	this->fecha = fecha;
	this->hora = hora;
	this->sismos = sismos;
	this->lluvias = lluvias;
	this->visibilidad = visibilidad;
}

eclipse::~eclipse() {}

string eclipse::getTipo() { return tipo; };
string eclipse::getFecha() { return fecha; };
int eclipse::getHora() { return hora; };
bool eclipse::getSismos() { return sismos; };
bool eclipse::getLluvias() { return lluvias; };
string eclipse::getVisibilidad() { return visibilidad; };

void eclipse::setTipo(string tipo) { this->tipo = tipo; };
void eclipse::setFecha(string fecha) { this->fecha = fecha; };
void eclipse::setHora(int hora) { this->hora = hora; };
void eclipse::setSismos(bool sismos) { this->sismos = sismos; };
void eclipse::setLluvias(bool lluvias) { this->lluvias = lluvias; };
void eclipse::setVisibilidad(string visibilidad) { this->visibilidad = visibilidad; };

void eclipse::toString() {
	cout << "TIPO: " << this->tipo << " | FECHA: " << this->fecha << " | HORA: " << this->hora << " | SISMOS: " << this->sismos << " | LLUVIAS: " << this->lluvias << " | VISIBILIDAD: " << this->visibilidad << endl;
}