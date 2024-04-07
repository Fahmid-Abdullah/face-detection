@echo off
call conda activate base
cd /d %~dp0
python face_recognition.py %*
pause
