# 🏢 Sistema Integral de Gestión de Operaciones - Software FJ

## 👤 Desarrollador
* **Estudiante:** Manuel Antonio Vargas Quezada  
* **Curso:** Programación Orientada a Objetivos (POO) - UNAD  

---

## 🎯 Descripción y Objetivos del Proyecto

Este sistema fue desarrollado para automatizar y controlar de forma segura el portafolio de servicios tecnológicos de la empresa **Software FJ**, el cual abarca el alquiler de infraestructura, la reserva de espacios físicos y consultorías cloud. 

El propósito principal del software es garantizar que ninguna transacción ponga en riesgo la estabilidad de la aplicación o la integridad de los datos personales de los clientes, resolviendo los siguientes objetivos:
* **Estabilidad Operacional:** Mantener el sistema en ejecución continua mediante un control estricto de flujos e ingresos erróneos en la terminal.
* **Rigores de la POO:** Aplicar encapsulamiento privado para la protección de datos sensibles, herencia estructural para los servicios y polimorfismo puro en la liquidación de tarifas.
* **Persistencia Local:** Asegurar un canal de auditoría física para el negocio registrando cada evento relevante en tiempo real.

---

## ⚠️ Arquitectura del Manejo de Excepciones

Para evitar que la aplicación sufra caídas inesperadas ante datos inválidos o malas interacciones del usuario en la consola, implementamos una estrategia de robustez dividida en tres alarmas principales:

* **`ErrorCliente`:** Controla errores en la capa de datos personales, impidiendo registros con identificaciones alfanuméricas inválidas, nombres vacíos o correos sin el formato requerido.
* **`ErrorServicio`:** Restringe la manipulación de tarifas base, asegurando que ningún servicio opere con valores menores o iguales a cero.
* **`ErrorReserva`:** Ataja inconsistencias en la lógica del tiempo, controlando que no existan duraciones negativas y bloqueando intentos de duplicar la cancelación de una misma orden.

> 💡 **Nota de Ingeniería:** Todo este ecosistema se sostiene sobre estructuras `try / except`, utilizando variantes con `else` y `finally` para asegurar el cierre limpio de los procesos y la liberación segura de memoria en la terminal.

---

## 📂 Sistema de Auditoría y Registro de Logs

El software no depende de bases de datos externas; en su lugar, utiliza un sistema de persistencia física e inmediata:

* **Archivo de Bitácora (`logs.txt`):** Cada vez que ocurre un evento exitoso o un fallo controlado, el sistema abre, escribe y salva la novedad de forma automática. Esto permite estudiar el historial de uso y revisar las 10 simulaciones obligatorias exigidas por la rúbrica sin interrumpir la experiencia del usuario.

---

## ▶️ Guía de Ejecución en Consola

Para poner en marcha los componentes del sistema en cualquier portátil, ejecute los siguientes comandos en la terminal de Visual Studio Code:

**Arrancar la aplicación interactiva (Menú Principal):**
```bash
python main.py