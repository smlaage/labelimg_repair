<b>labelimg_repair.py</b>

The application labelImg is a popular tool to create labels (annotations) to images as required 
for object detetcion training images, e.g. using TensorFlow. See: https://github.com/HumanSignal/labelImg.
The labelImg application offers a handy point and click selection of relevant parts of the images
and creates rectangles that are saved as XML files. Unfortunately, the last published version of 
labelImg crashes due to data type conflicts. 

This script repairs the labelImg application on your local machine. Once labelImg is installed
(e.g. by pip install labelimg), this script repairs the type error. It scans through the files
'canvas.py' and 'labelImg.py' and converts the arguments for drawLine(), drawRect() and 
setValue() calls to int data types. That's all. Please note that the sript requires write access
to the files 'canvas.py' and 'labelImg.py'. 

Usage:
- run the script from within a python IDE (e.g. Thonny) or at the command prompt
- provide the path to the lcoal labelImg installation

Example:
python labelimg_repair.py C:\Users\xyz\AppData\Local\Programs\Thonny\Lib\site-packages

SLW 2024-04
