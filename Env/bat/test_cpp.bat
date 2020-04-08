@echo off

cl ..\src\Main.cpp

echo #############################################
echo Input :
echo #############################################
type ..\input\input.txt
echo #############################################
echo Output :
echo #############################################
Main < ..\input\input.txt
echo #############################################
del Main.exe
del Main.obj