import java.io.*;
import java.util.*;

public class grading {

  public static void main(String[] args) {
    Scanner keyboard = new Scanner(System.in);
    int numGrades = keyboard.nextInt();
    int goal = keyboard.nextInt();
    int[] gradesArray = new int[numGrades];
    double[] weightArray = new double[numGrades];
    for (int i = 0; i < numGrades; i++) {
      gradesArray[i] = keyboard.nextInt();
    }
    double remainingWeight = 1;
    for (int i = 0; i < numGrades; i++) {
      weightArray[i] = keyboard.nextDouble();
      remainingWeight -= weightArray[i];
      //remainder -= keyboard.nextDouble();
    }
    double total = 0;
    for (int i = 0; i < numGrades; i++) {
      total += (weightArray[i] * gradesArray[i]);
      //remainder -= keyboard.nextDouble();
    }
    double answer = goal - total;
    answer = answer / remainingWeight;

    answer = Math.ceil(answer);

    System.out.println((int)answer);

    keyboard.close();
  }
}