# Program Name: pirate.py
# Purpose of a program:
# User can be screened by the greeting message user enters as: a pirate or pirate hater
# Pirates greet each other with a password.
# If the greeting is matched to Arrr!,the user is identified as a pirate.
# Otherwise, the user is a hater of pirates.
########################################################################################
# Noble Bautista = Editor

greeting = input("Hello, possible pirate! What's the password?") #asks for user input (password)
if greeting == ("Arrr!"): #only specified password option that will "deny" access
	print("Go away, pirate.")
else:
	print("Greetings, hater of pirates!") #anything typed that is not "Arrr!" will be "accepted" + given this greeting in print statement
