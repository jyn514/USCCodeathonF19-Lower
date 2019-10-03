# Truth Table Generator

Truth tables are used to see every possible combination of true and false values of n number of variables. 

## Description

Truth tables generally have the appearance 
```
A B 
F F 
F T 
T F 
T T 
```
where the variable names, in this case 'A' and 'B', are on the first line.
Below each variable, are rows of T's and F's. An 'F' stands for false, while 'T'
stands for true. The first row (that being the first row below the variable names) will always start with all of the variables being false (meaning under each variable is an 'F'). When moving to the next row, the farthest right 'F' is always changed to a 'T'.
When this happens, all of the T values to the right of the changed value are changed to F. So if a line showed
```
F T F T F
```
the next row would be
```
F T F T T
```
(changing farthest right 'F' to a T. In this case nothing is to the right of the changed truth value).

Then after that would be
```
F T T F F
```
this is achieved by changing the farthest right 'F', in this case is the third column from the left, to a 'T'. This caused all of the 'T's to the right of it to be changed to 'F's

## Input

The first line contains an integer $$n$$, the number of variables to have in the truth table

The second line contains an integer $$r$$, the row number that should be printed (with the 
row below the variable names being row number 0)

## Constraints

$$1 \leq n \leq m$$, where m \leq 30

$$0 \leq r \le 2^m$$

## Ouput

Print the truth values from left to right of row $$r$$, with spaces between T's and F's 



### Sample Input 0

```
3
5
```

### Sample Output 0

```
T F T
```

### Explanation 0

The entire truth table for 3 variables (with line numbers added just for the explanation) is as follows, with line 5 having an arrow

```
  A B C 
0 F F F 
1 F F T 
2 F T F 
3 F T T 
4 T F F 
5 T F T <-----
6 T T F 
7 T T T 
```



### Sample Input 0

```
4
14
```

### Sample Output 1

```
T T T F
```

### Explanation 1
The entire truth table for 4 variables (with line numbers added just for the explanation) is as follows, with line 14 having an arrow

```
   A B C D
0  F F F F
1  F F F T
2  F F T F
3  F F T T
4  F T F F
5  F T F T
6  F T T F
7  F T T T
8  T F F F
9  T F F T
10 T F T F
11 T F T T
12 T T F F
13 T T F T
14 T T T F <-------
15 T T T T
```