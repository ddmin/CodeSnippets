# Chess (from Scratch)

A chess game made from scratch using absolutely no dependencies. 


# Progression

10/5 - Created classes for each Piece

12/21 - Functionality to move pieces

12/28 - Started Board Class and moved Chess pieces to seperate file

12/29 - Pawn Movement logic

12/30 - Change Pawn Movement logic and make possibleMove method, En Passant handling, 
        Changed CLI to show both boards

1/3 - Board class has history, can record game to txt file

1/4 - FINALLY FINISHED EN PASSANT BY USING BOARD HISTORY. 
      IT TURNS OUT THAT KEEPING TRACK OF movedTwoSpaces AS A VARIABLE IS NOT A GOOD IDEA
      BECAUSE EN PASSANT ONLY WORKS AFTER ONE TURN. I AM TYPING IN ALL CAPS TO EXPRESS MY FRUSTRATION.
      NONE OF THE OTHER PIECES WILL BE AS INFURIATING AS MAKING THE PAWN CLASS.

1/5 - Finished Rook Class

1/6 - Scratch that en passant triggers if any pawn is moved two spaces. To fix this you have to see if
      the pawn in question is the correct pawn or not. En Passant should be all patched up. But then again.

1/7 - Finished Bishop class. Added Tuple to Piece Notation translator in order to help debug.

1/8 - Finished Knight class.

1/11 - Finished Queen Class

1/12 - Finished King Class

1/13 - Stopped tracking chess_games with git, because it changes every single time I want to test the code. Also made it so that "Game Files" directory is automatically created.

1/25 - Honestly this is too much work. There is already a python chess library. Might as well make a game from that. 

# TODO

Board Class

* Record piece captures, checks (# CAPTURE, # CHECK, # MATE)
* Handle Castling (def castle(self, side, player)) where side is either king side or queenside and player is the player

Piece Class

* Handle Checks and actual gameplay

General

* Better CLI (1. Make Move 2. Exit 3. Record Game)
* Handle Castling
* Handle Checks, Checkmate, Stalemate
* Keep track of number of pieces
* Add a gif to README
* Make better user input (ie only let them enter letter and then number probably something similar to CUTIE)