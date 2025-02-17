# Collections Module

```python
from collections import Counter

numbers = [8, 6, 9, 5, 4, 5, 5, 4, 5, 8, 7, 3]
print(Counter(numbers))
print(Counter("Jorge Rubio Miss"))
phrase = "al pan pan y al vino vino"
print(Counter(phrase.split()))

serie = Counter([1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3])
print(type(serie))
print(type(serie))
print(serie.most_common())  # Tuples with numbers and their appearances
print(serie.most_common(1))  # Number that most appearances

from collections import defaultdict

mi_dic = {"uno": "verde", "dos": "azul", "tres": "rojo"}
print(mi_dic["dos"])

mi_dic = defaultdict(lambda: "nada")

mi_dic["uno"] = "verde"
print(mi_dic["dos"])

from collections import namedtuple

my_tuple = (500, 18, 65)
print(my_tuple[1])

Person = namedtuple("Person", ["name", "height", "weight"])
ariel = Person("Ariel", 1.76, 79)

print(ariel.height)
```

# OS and Shutil modules

```python

import os
import shutil

path = "/home/jorgerxbio/downloads/"

for directory, subdirectory, file in os.walk(path):
    print(f"In directory: {directory}")
    print(f"subdirectories: ")
    for sub in subdirectory:
        print(f"{sub}")
    print("Files are: ")
    for f in file:
        print(f"\t{f}")
    print("\n")
```

# Datetime Module

```python
import datetime

my_hour = datetime.time(17, 35, 50, 1500)
print(type(my_hour))
print(my_hour)
print(my_hour.minute)
print(my_hour.hour)
```

```python
my_day = datetime.date(2025, 10, 17)
print(my_day)
print(my_day.ctime())
```

```python
from datetime import date, datetime

my_date = datetime(2025, 5, 15, 22, 10, 15, 2500)
my_date = my_date.replace(month=11)
print(my_date)

birth = date(1995, 3, 5)
death = date(2095, 6, 19)

life = death - birth
print(life)
print(life.days)

wake_up = datetime(2022, 10, 5, 7, 30)
sleep = datetime(2022, 10, 5, 23, 45)

vigil = sleep - wake_up

print(vigil)
print(vigil.seconds)
```

# Time

```python
import time
import timeit


def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista


inicio = time.time()
prueba_for(15000)
final = time.time()

print(f"time: {final-inicio}")

inicio = time.time()
prueba_while(15000)
final = time.time()
print(f"time: {final-inicio}")
```

# Math

```python
import math

resultado = math.floor(89.665)
print(resultado)

resultado = math.ceil(89.665)
print(resultado)

resultado = math.pi
print(resultado)

resultado = math.log(100, 2)
print(resultado)

resultado = math.tan(250)
print(resultado)

resultado = math.cos(250)
print(resultado)
```

# Regular Expresions Module

/d - numeric digit - v\d.\d\d
/w alphanumeric character - \w\w\w-\w\w
/s blank space - number\s\d\d
/D No numeric - \D\D\D\D
/W No alphanumeric - \W\W\W
/S No blank space -\S\S\S\S

```python
import re

texto = "Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online"

palabra = "ayuda" in texto
print(palabra)

patron = "ayuda"
busqueda = re.search(patron, texto)
print(busqueda)
if busqueda != None:
    print(busqueda.start())

busqueda = re.findall(patron, texto)
print(busqueda)
if busqueda != None:
    print(busqueda)

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
```

```python
import re

texto = "llama al 564-525-6588 ya mismo"

patron = r"\d\d\d-\d\d\d-\d\d\d\d"

resultado = re.search(patron, texto)
print(resultado)
if resultado != None:
    print(resultado.group())

print("\n----------------------------------------\n")
patron = r"\d{3}-\d{3}-\d{4}"
resultado = re.search(patron, texto)
print(resultado)
if resultado != None:
    print(resultado.group())

patron = re.compile(r"(\d{3})-(\d{3})-(\d{4})")
resultado = re.search(patron, texto)
print(resultado)
if resultado != None:
    print(resultado.group(2))  # Select a group
```

```python
import re

texto = "No atendemos los martes por la tarde"

buscar = re.search(r"lunes|martes", texto)  # Logic operators

print(buscar)

buscar = re.search(r".demos", texto)  # Logic operators
print(buscar)

buscar = re.search(r"....demos", texto)
print(buscar)

buscar = re.search(r"^\D", texto)  # ^ Check at the begin of the string
print(buscar)

buscar = re.search(r"\D$", texto)  # $ Check at the last of the string
print(buscar)

buscar = re.findall(r"[^\s]", texto)  # [] Exclude
print(buscar)

buscar = re.findall(r"[^\s]+", texto)  # [] Exclude print(buscar)
```

# Zip module

```python
import zipfile

mi_zip = zipfile.ZipFile("archivo_comprimir.zip", "w")

mi_zip.write("notes.md")

zip_abierto = zipfile.ZipFile("archivo_comprimir.zip", "r")
zip_abierto.extractall()
```
