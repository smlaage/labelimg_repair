labelimg_repair.py

This simple scripts applies to the labelImg package.
See: https://github.com/HumanSignal/labelImg

Once the package is installed on your local machine, the script repairs the type error
that occurs with the most recently published version of labelImg. The script requires write access
to the files 'canvas.py' and 'labelImg.py'. It scans through the files and converts the arguments
for drawLine(), drawRect() and setValue() calls to int data types. That's all.

Usage:
- run the script from within a python IDE (e.g. Thonny) or at the command prompt
- provide the path to the lcoal labelImg installation

Example:
python labelimg_repair.py C:\Users\xyz\AppData\Local\Programs\Thonny\Lib\site-packages

SLW 2024-04
