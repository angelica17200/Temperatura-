"""
problema No 3: conversion de grados celcius a farenheit"""

print ("----------------------------------------------------")
print ("-------conversion de grados celcius a farenheit-------")
print ("----------------------------------------------------")

# Input 
c= input("digite los grados c:")
c= int(c)

# Processing 
k= c + 273.15
f= 1.8 *c + 32

# output 
print("\nResultado\n")

print( str (c) + " grados celcius es igual a: " + str (f) + " grados farenheit")
print( str (c) + " grados celcius es igual a: " + str (k) + " grados kelvin ")

