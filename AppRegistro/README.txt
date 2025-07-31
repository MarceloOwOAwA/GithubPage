Preparativos
	Descargar PostulacionMarceloOrdenes.7z 
	Descomprimir PostulacionMarceloOrdenes.7z 

	Instalar Python Powershell
		winget install python
	Instalar Docker desde pagina web
		https://www.docker.com/products/docker-desktop/
---------------------------------------------------------------------------------
Ejecutar aplicacion de forma manual
	Abrir Powershell

	Dirigirse a la carpeta 
		PostulacionMarceloOrdenes\Docker,Api,MongoDB

	Ejecutar entorno virtual 
		python -m venv venv

		.\venv\Scripts\Activate.ps1
	Dirigirse a la carpeta 
		PostulacionMarceloOrdenes\Docker,Api,MongoDB\user_api\user_api
	Ejecutar comando powershell
		docker compose up --build
	Dirigirse a pagina
		http://localhost:8000/docs 
	Correr aplicacion python ubicada en 
		PostulacionMarceloOrdenes\AppRegistro
---------------------------------------------------------------------------------
Ejecutar aplicacion con script
	Abrir Powershell
	Dirigirse a la carpeta 
		PostulacionMarceloOrdenes
	Correr el script con el comando
		.\iniciar_entorno.ps1
