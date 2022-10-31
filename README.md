# code_to_image
# 🌐 Converting Python files to PNG using Python
# Before
![before](https://github.com/lidskiyq/code_to_image/blob/main/code.jpg)
# After
![after](https://github.com/lidskiyq/code_to_image/blob/main/test.png)

Unistall lib:
```
$ pip install pytoimage
```
```
pip install pathlib
```
Inside func "pycode_to_img":
Check if our file is True:
```
path = Path(file_path)
    
if not path.is_file():
    return 'Ups... please check a file path! :/'
```
Create object PyImage and dictionary with palette:
```
code = PyImage(file_path, background=(255, 255, 255))
palette = {
    'line': (255, 0, 255), #color of string numbers
    'normal': (0, 0, 0) #text color
    }
```
Set our palette:
```
code.set_color_palette(palette=palette)
code.generate_image()
```
Save our file and print if all good:
```
code.save_image(img_name)   
return f'{img_name} saved successfully!'
```
In main fuction input file name and call our func:
```
def main():
    file_path = input('Please enter a filename: ')
    print(pycode_to_img(file_path=file_path))
```
