@echo off
title Iniciando registro automático (Flask + Web)
echo --------------------------------------
echo  L A N Z A N D O   S I S T E M A  👇
echo --------------------------------------

REM Abrir el servidor Flask
echo Iniciando servidor Flask...
start cmd /k "cd /d C:\Users\stsda\OneDrive\Escritorio\retro-registro && python app.py"

REM Esperar 3 segundos
timeout /t 3 > nul

REM Abrir index.html en el navegador
echo Abriendo página principal...
start "" "C:\Users\stsda\OneDrive\Escritorio\retro-registro\public\index.html"

exit
