#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

timer = int(input("Ingrese un número mayor a cero: "))


while True:
	print(timer)
	timer -= 1
	time.sleep(1)
	
	if timer == 0:
		print("¡¡¡ BOOM !!!")
		break
