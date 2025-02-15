# Open and modify files

```python
my_file = open("test.txt")
print(my_file)
# print(my_file.read())

print(".: readline :.")
line = my_file.readline()
print(line.rstrip())  # rstrip is for ignore \n

for l in my_file:
    print("Here say: " + l)

print(".: readlines :.")
print(my_file.readlines()) # Print a list with every line

my_file.close()
```

# Read and write files

```python
file = open("test.txt", "w")
file.write("I am the new text\n")
file.write("Second line hehe\n")
file.write("Third line hehe\n")
file.writelines(["hello", "world", "here", "i", "am"])
file.close()

file = open("test.txt", "a")
file.write("ya llegó tu papi paty")
file.close()

file = open("test.txt", "r")
print(file.read())
file.close()
```

# Path

```python
import os

path = os.getcwd()  # Get actual directory
path = os.makedirs("/home/jorgerxbio/Repositories/python-courses/other_directory")
path = os.rmdir("/home/jorgerxbio/Repositories/python-courses/other_directory")
path = os.chdir("/home/jorgerxbio/Repositories/python-courses/")

file = open("other_text.txt")
print(file.read())
print(path)

path = "/home/jorgerxbio/Repositories/python-courses/other_text.txt"
element = os.path.basename(path)
print(element)

element = os.path.dirname(path)
print(element)

element = os.path.split(path)
print(element)

# How to create paths for all operating systems
from pathlib import Path

directory = Path("/home/jorgerxbio/Repositories/python-courses/")
file = directory / "other_text.txt"

my_file = open(file)
print(my_file.read())
```

# Pathlib

```python
from pathlib import Path, PureWindowsPath

path = Path(
    "/home/jorgerxbio/Repositories/python-courses/programador-avanzado-en-16-dias/test.txt"
)
print(path)
print(path.read_text())
print(path.name)  # File name
print(path.suffix)  # File suffix
print(path.stem)  # File name withour suffix

if not path.exists():
    print("This file don't exists")
else:
    print("This file exists")

# How to transform a path to a Windows path
windows_path = PureWindowsPath(path)
print(windows_path)
   print("This file exists")
```

```python
from pathlib import Path

path = Path(
    "/home/jorgerxbio/Repositories/python-courses/programador-avanzado-en-16-dias/test.txt"
)
guide = Path("Barcelona", "Sagrada_Familia.txt")  # This is a relative path
print(guide)

# How to get the absolute path for a specific site in my sistem?
base = Path.home()
print(base)

guide = Path(
    base, "Europe", "Spain", Path("Barcelona", "Sagrada_Familia.txt")
)  # This is a relative path
print(guide)

guide2 = guide.with_name(("La_Pedrera.txt"))
print(guide2)

print(guide.parent) # Allow us to get the parent of current directory
print(guide.parent.parent)
```

```python
from pathlib import Path

# How to print all txt that are into a directory
guide = Path(Path.home(), "Repositories", "Europa")

for txt in Path(guide).glob("*.txt"):
    print(txt)

print(" .: ----- :. ")
for txt in Path(guide).glob("**/*.txt"):
    print(txt)

guide = Path("Europa", "España", "Sagrada_Familia.txt")
en_europa = guide.relative_to(Path("Europa"))
en_espania = guide.relative_to(Path("Europa", "España"))

print(en_europa)
print(en_espania)
```

# Clean console

```python
from os import system

name = input("What is your name: ")
age = input("How old are you: ")

system("clear")
print(f"Your name is {name} and you're {age} year old")
```

# files and functions

```python
def registro_error(my_file):
    file = open(my_file, 'a')
    file.write('se ha registrado un error de ejecución')
    file.close()
```
