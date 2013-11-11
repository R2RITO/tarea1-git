#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import string

def main():
    #Main principal del programa 

    if len(sys.argv) < 2:
	    #Verificamos si se ingresaron todo los argumentos
        print("Argumentos insuficientes, favor introduzca el archivo")
        return
 
    #Apertura del archivo
    try:
        fd = open(sys.argv[1],'r')

    #Revisamos que el archivo exista en el directorio
    except IOError:
        print "--ERROR-- El archivo no existe en el directorio"
        sys.exit()

    #Se lee el archivo y se almacena en una variable
    data = fd.read()
    palabras = data.split('\r\n')
    abc = list(string.uppercase)
    print abc

    for p in palabras:        
        for a in abc:
            if (a+a) in p:
                abc.remove(a)


    print abc
        
    


if __name__ == "__main__":
    sys.exit(main())
