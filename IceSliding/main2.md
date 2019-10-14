While on his adventure, Gilver finds himself in an ice cave that seems to be on a grid pattern made of ice, solid objects, and energy bars.

When Gilver walks on the ice, he continues moving in the same direction until he hits a solid objct or the edge of the cave. Solid objects are shown as 1, empty spaces are shown as '0'.

Gilver also has "energy points". Each time he moves to a new tile, he loses 1 energy point. There seems to be energy bars on the ground of the cave, denoted by single letters of the alphabet.

The amount of energy points that Gilver gets from being on the same tile as the letter is equal to the letter's position in the alphabet (A=1, B=2, C=3...Z=26). If the letter is evenly divisible by 3, the amount of points that it gives Gilver is divided by 2, rounded up (so C has a starting value of 3, divided by 2 would give 2 in this case (3/2=1.5, rounded up)). If Gilver is ever on the same tile as a letter, he gets the energy and the letter disappears.

Gilver has a max of 30 energy points. So if he has 25 points, then moves 1 space that has a letter 'z', his energy would go to 24, then to 30.

Input Format

The first line will consist of three numbers   and , in that order, where  is the width of the cave from the left to the right,  is the height from top to bottom, and  is Gilver's starting energy.

The next  lines of  length will be what the cave looks like, made of 0s, 1s, a 2, and letters of the alphabet. 0s are icy spots, 1s are solid objects, the 2 is the current position of Gilver, and the letters are energy bars. The rest of the lines after will be the instructions given to Gilver, either 'left', 'right', 'up', or 'down'. (no quotes)

Constraints

, ,

The starting value for : 

Output Format

Output the ending coordinates   and amount of energy  that Gilver had at the end of the instructions with 0,0 being in the bottom left [first column, bottom row]