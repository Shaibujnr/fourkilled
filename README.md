fourkilled
==========

A text-based number guessing game
.
.
.
.
4killed is a Brain Training Game that deals with a set of 4 numbers ranging from 
one to nine. These 4 numbers are unique i.e no number is repeated in these four 
numbers. The aim of the game is for the player to guess these four numbers 
exactly as they are in value and position (1st, 2nd, 3rd and 4th) from the left. 
Each number in the players guess is taken and compared with these four unique 
numbers and then a result is returned. The player keeps guessing until he gets 
these numbers exactly as they are in value and in position. The results are 
returned in terms of killed(k), injured(i) and none(n).

A number in the player's guess is said to be killed if that number is equivalent
to that in the unique numbers in value and in position; Also a number is said to 
be injured if in the unique numbers, there is such a value but not in the same 
position as guessed by the player; And a number is said to be none if there is 
no such value in the unique numbers. for example
        
        unique_number= 6758
        players_guess= 5762
        result would be 1k2i1n
        
The game is over once the player guesses the unique numbers correctly of course 
in value and in position. In other words the aim of this game is for the player 
to hit a 4killed!!

NOTE ::::::
Only the results will be returned there shall be no hint as to which of the 
numbers is killed, injured or none.

ENJOY!!!

:: To quit enter Q

.
.
.
.
.
.
.
fourkilled(GUI with Kivy)
========================

Well since i'm new to kivy and it is really really fun. I decided to use kivy for 
the gui of this game because firstly i'd like to test my skill and whenever i think
of 4killed it makes more sense as a mobile game and since kivy supporsts quite a few
mobile platform especially android and ios i felt this is a good start. 




