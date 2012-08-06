#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# primeiro.py - nosso primeiro programa python

import random

numero = random.randint(1,100)

tentativas = 0
escolha = 0

while escolha != numero:
	tentativas += 1
	escolha = input("Informe o numero até 100:  ")
	if escolha > numero:
		print "Maior"
	elif escolha < numero:
		print "Menor"

print "acertou congrats " ,   numero
print	"voce usou ", tentativas, "tentativas"

