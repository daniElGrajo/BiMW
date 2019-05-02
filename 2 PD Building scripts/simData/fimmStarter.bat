:: This script is intended to initialize FIMMWAVE 
:: using the TCP/IP capabilities which will allow
:: script execution.
:: Daniel Grajales. March 2014
:: ICN2. Nanobiosensors and bioanalytical applications

::set the path where phtonDesign is installed
set FIMMWAVEPATH="C:\Program Files (x86)\PhotonD\Fimmwave\bin32"

cls
:: Just FYI
echo "executing FIMMWAVE with TCP listening on port 5101"

:: Execute with parameter pt (port) listening on port 5101 (tcp ip)
start "" %FIMMWAVEPATH%\fimmwave.exe "-pt" 5101

