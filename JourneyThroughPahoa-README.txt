#Noble Bautista
#December 1st, 2022
#CSS-225
#Journey Through Pahoa v1.0


***GENERAL INFORMATION***

"Journey Through Pahoa" is a short text-based adventure game centered around making a series of decisions in order to make it out of the wilderness alive and back home safe and sound.

"Journey Through Pahoa" is posted on Github, and distributed manually via Noble Bautista and other owners of "Journey Through Pahoa" including National Louis University.

"Journey Through Pahoa" uses no external services, and exclusively operates on the Python coding language.


***SYSTEM REQUIREMENTS***

"Journey Through Pahoa" is capable of operating on any computer capable of running the Python coding language. If python is not installed, please visit https://python.org to download.

To run "Journey Through Pahoa," Run Main.py. All other files are submodules that Main.py uses in order for the game to run. 

While playing, the user will be given a series of written passages and scenarios that will be paired with input prompts. 

As the user answers these prompts, they will traverse the game by either succeeding and moving forward in the chapters, being temporarily sent back to previous chapters, or terminated all together depending on their selection.


***CODE INFORMATION***

The structure of "Journey Through Pahoa" is fundamentally reliant on rudimentary Python coding structures. 

Overall, it is based on functions that include a series of if and while statements that are programmed to run differently depending on the user's selection.

Below is a list of each .py file within the "Journey Through Pahoa" game with a brief description of their purpose/function.


***Main.py: loads Main() which calls game_intro() within function.

***Chapter1.py: loads Main1() which calls Chapter1_intro. Includes references to four other possible results (functions) 

***Chapter2.py: loads Main2() which calls Chapter2_intro. Includes references to four other possible results (functions)

***Chapter3.py: loads Main3() which calls Chapter3_intro. Includes references to four other possible results (functions)

***Chapter4.py: loads Main4() which calls Chapter4_intro. Includes references to three other possible results (functions), which include more options within said functions

**Chapter5.py: loads Main5() which calls Chapter5_intro. Includes references to three other possible results (functions), which include more options within said functions


***gameover.py: The module that is referenced whenever a player choses an option that terminates their journey.
