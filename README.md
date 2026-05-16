# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

## Integrante
* Manuel Antonio Vargas Quezada

## Objetivos del Sistema
* Garantizar la modularidad, estabilidad y continuidad del sistema Software FJ.
* Implementar con rigor los pilares POO de abstracción, encapsulamiento, herencia y polimorfismo.
* Asegurar la persistencia local de eventos y fallos mediante el uso de archivos físicos de logs.

## Estructura del Sistema (Arquitectura de Software)
El proyecto sigue una estructura modular limpia dividida por responsabilidades:

```text
Proyecto_Fase4_Programacion/
│
├── clases/                  # Capa de Lógica de Negocio y Entidades
│   ├── excepciones.py       # Definición de alarmas y errores personalizados
│   ├── cliente.py           # Entidad del usuario con encapsulación de datos
│   ├── servicio.py          # Clase abstracta y servicios derivados (Salas, Equipos, Asesorías)
│   └── reserva.py           # Clase integradora y motor de polimorfismo
│
├── pruebas/                 # Capa de Aseguramiento de Calidad (QA)
│   └── pruebas.py           # Suite de test unitarios automatizados
│
├── logs.txt                 # Archivo físico de persistencia de eventos y fallos
├── main.py                  # Orquestador principal e interfaz de usuario (CLI)
└── README.md                # Documentación técnica del sistema
python main.py
python -m unittest pruebas/pruebas.py