@REM execute node xrhash.js every 3 seconds
echo off
echo executing...
:executor
node xrhash.js
ping 127.0.0.1 >nul
goto executor