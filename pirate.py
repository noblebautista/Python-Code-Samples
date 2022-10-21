# Program Name: pirate.py
# Purpose of a program:
# User can be screened by the greeting message user enters as: a pirate or pirate hater
# Pirates greet each other with a password.
# If the greeting is matched to Arrr!,the user is identified as a pirate.
# Otherwise, the user is a hater of pirates.
########################################################################################
# Noble Bautista = Editor

greeting = input("Hello, possible pirate! What's the password?")
if greeting == ("Arrr!"):
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!")
