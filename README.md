# ModbusSimulatorServer

GUIDA INSTALLAZIONE

MODBUS SERVER + SIMULATORE MACCHINARIO
1.	Installare sul Raspberry Pi il sistema operativo Raspberry Pi OS.
Ulteriori info: https://indomus.it/guide/come-installare-e-configurare-raspberry-pi/#tool

2.	Installare da terminale l’ambiente di sviluppo python IDLE:
sudo apt-get update  
sudo apt-get install python-dev  
sudo apt-get install python-pip  

3.	Installare da terminale la libreria pymodbus
pip install pymodbus

4.	Avviare il programma python “serverModbus.py” https://github.com/simone99n/ModbusSimulator/blob/main/Server/serverModbus.py

5.	Il Simulatore Server Modbus è avviato!

MODBUS CLIENT + WEB APPLICATION
1.	Avviare da un ambiente di sviluppo Java il programma https://github.com/simone99n/ModbusSimulator/tree/main/Client/Client

2.	Il Client Modbus e la Web Application sono avviati!

3.	Le  API si trovano all’indirizzo http://locahost:8080/api/v1/client/

      3.1.	POST: api/v1/client/writeSingleRegister passare i valori ip, startingAddress e value

      3.2.	POST: api/v1/client/writeSingleCoil passare i valori ip, startingAddress e value

      3.3.	POST: api/v1/client/writeMultipleRegisters passare i valori ip, startingAddress e values

      3.4.	POST: api/v1/client/writeMultipleCoils passare i valori ip, startingAddress e values

      3.5.	GET:   api/v1/client/readInputRegister passare i valori  ip, startingAddress e quantity

      3.6.	GET:   api/v1/client/readHoldingRegister passare i valori  ip, startingAddress e quantity

      3.7.	GET:   api/v1/client/readDiscreteInput passare i valori  ip, startingAddress e quantity

      3.8.	GET:   api/v1/client/readCoils passare i valori  ip, startingAddress e quantity



Per inviare comandi REST API si consiglia il software Postman: https://www.postman.com/
