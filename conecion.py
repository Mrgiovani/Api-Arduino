import json
import serial
import requests
port =serial.Serial('COM3',9600)
while True:
    print("Ingrese el nombre de su mascota: ")
    nombre = input()
    print("Ingrese nombre del dueño ")
    usuario = input()
    data=(port.readline().decode('utf-8'))
    print(f'La estatura de {nombre} es: {data}')
    respuesta = requests.post('https://register-api-tres.herokuapp.com/estatura',json={'mascota':nombre,'estatura':data,'usuario':usuario})
    #print(respuesta)
    #print(type(data))
    