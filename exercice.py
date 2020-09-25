#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def is_even_len(string):
      return len(string) % 2 == 0

def get_num_char(string, char):
    	num_char = 0 
		for c in string:
    		num_char += 1 if c == 0 else 0
	  return num_char


def get_first_part_of_name(name):
    	first_part = name.split('-')[0]
		capitalized = first_part[0].upper() + first_part[1:]	
	return "Bonjour, " + capitalized


def get_random_sentence(animals, adjectives, fruits):
    	animal_index = [random.randrange(0, len(animals))]
		animal_word = animal[animal_index]

		ajd_index = random.randrange(0, len(animals))
etc
	return f"Aujourd'hui, j'ai vu un [animal_world] s'emparer d'un panier [adj] plein de [fruits]. "
	return ""

if __name__ == "__main__":
	spam = "Bonjour!"
	parity = "pair" if is_even_len(spam) else "impair"
	print(f"Le nombre de caractère dans la chaine '{spam}' est {parity}.")

	eggs = "Hello, world!"
	print(f"Le nombre d'occurrence de l dans '{eggs}' est : {get_num_char(eggs, 'l')}.")

	parrot = "jean-marc"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "bananes")
	print(get_random_sentence(animals, adjectives, fruits))
