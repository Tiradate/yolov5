ECHO ON
REM A batch script to execute a Python script
SET PATH=%PATH%;C:\Users\pc\EagleEyes\yolov5
call cd C:\Users\pc\EagleEyes\yolov5
call conda init powershell
call conda activate EagleEyes
python EagleEyes.py
PAUSE