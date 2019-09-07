# Test Day

Professor Smith has decided to release the scores for his CS102 course. He also
forgot to include extra credit. Instead he has decided to ask his students to
write a program that can calculate how many points the student needs to score on
their test to score an $$n$$ in the course given the weights and previous test
scores. The final test will be worth the remainder of the weights, such that,  
$$\sum score_1 score_2 \dots score_n = 1$$

## Description

Given a number of tests and goal score on the first line. The scores space delimmited on the
second line, and the weights space delimmited on the last line. What score,
rounded up to the nearest integer (ex. $$3.4 \rightarrow 4$$, and $$-3.4
\rightarrow -3$$), is needed to get the finish the class with $$goal$$ final
grade.

## Input

```
$$n$$  $$goal$$
$$score_1$$ $$score_2$$ $$\dots$$ $$score_n$$
$$weight_1$$ $$weight_2$$ $$\dots$$ $$weight_n$$
```

## Constraints

$$0 \leq n \leq 10^2$$   
$$0 \leq score_i, goal \leq 100$$   
$$0 \leq weight_i \leq 1$$ u


## Output
Print the integer necessary to score a $$goal$$ in Professor Smith's course.

### Sample Input 0

```
3 90
75 99 85
0.2 0.2 0.2
```

## Sample Output 0

```
96
```
