# Star Gazing

When looking up at the stars in the sky, Sal The Star Gazer notices that
the stars form grids, and within those grids, certain patterns are made. 




## Description

Sal decides that certain patterns should be worth certain amounts of points so that he can brag to his fellow sky looker, Gary The Galaxy Watcher, about the points he got while watching stars.
To account for the fact that some of the patterns overlap, he will only count the pattern that is worth the most amount of 
points. The point values for each pattern have nothing to do with the grid size, just the pattern itself. Each grid is guaranteed to have one of the patterns identified below. The stars are also always in a grid that is an odd by odd size. 
The stars only form one of the patterns shown below, with no extra stars. All patterns require having 1's and 0's as described / shown.



The "X" pattern is worth 20 points. This pattern has stars along the diagonals that go through the center, meaning the upper left corner to bottom right corner, and bottom left corner to upper right corner.
```
100000001
010000010
001000100
000101000
000010000
000101000
001000100
010000010
100000001
```

The "border" pattern is worth 18 points. It has a star at every edge position, 
going around the entire border of the grid.
```
111111111
100000001
100000001
100000001
100000001
100000001
100000001
100000001
111111111
```

The "plus" pattern is worth 15 points. It has a column of stars going through the center and a row of stars going through the center.
```
000010000
000010000
000010000
000010000
111111111
000010000
000010000
000010000
000010000
```

The 'checkerboard pattern' is worth 25 points. This one alternates stars and blank spaces, along rows and columns. The upper left and bottom right are always 1's
```
101010101
010101010
101010101
010101010
101010101
010101010
101010101
010101010
101010101
```

The 'corners' pattern is worth 30 points. It only has a single star in each corner of the grid.
```
100000001
000000000
000000000
000000000
000000000
000000000
000000000
000000000
100000001
```

The 'full board' pattern is worth 2 points. It has a star in every position on the board
```
111111111
111111111
111111111
111111111
111111111
111111111
111111111
111111111
111111111
```

## Input Format

The first line contains an integer $$n$$, where the grid is of size n by n. The second line onward will be the rows of the grid. 

## Constraints

$$3 \leq n \leq 10^4$$, where n is an odd number

## Ouput

Print the number of points that Sal got from the pattern

### Sample Input 0

```
7
1111111
1111111
1111111
1111111
1111111
1111111
1111111
```

### Sample Output 0

```
2
```

### Explanation 0

The entire board is filled up, so this is the full board pattern, which is worth 2 points. 


### Sample Input 1

```
3
101
010
101
```

### Sample Output 1

```
25
```

### Explanation 1

While this could be identified as the x pattern or checkerboard, Sal always chooses the option that gives him the most points. Since the chckerboard pattern is worth 25 points compared to the x pattern's 20 points, Sal identifies this as the checkerboard and gets 25 points.
