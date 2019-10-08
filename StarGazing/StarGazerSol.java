import java.util.Scanner;

public class StarGazerSol
{

public static void main(String[] args) {
    Scanner keyboard = new Scanner(System.in);

    String gridDimString = keyboard.nextLine();

    int gridDim = Integer.parseInt(gridDimString);
    int[][] grid = new int[gridDim][gridDim];
    String input = "";
    String currentNum = "";
    for (int y = 0; y < 3; y++) {
      input = keyboard.nextLine();
      for (int x = 0; x < gridDim; x++) {
        currentNum = input.substring(x, x + 1);
        grid[y][x] = Integer.parseInt(currentNum);
        // System.out.print(grid[y][x]);
      }

    }
    keyboard.close();

      // if true confirms x pattern or corners pattern or checkerboard
      if (grid[0][gridDim / 2] == 0) {

        if (grid[1][1] == 0) {
          // corners
          System.out.print(30);
        } else {
          if (gridDim == 3) {
            // checkerboard
            System.out.print(25);
          } else {
            if (grid[2][0] == 0) {
              // x pattern
              System.out.print(20);
            } else
              // checkerboard
                System.out.print(25);
          }
        }

      } else {
        // border or full board or plus

        if (grid[0][0] == 1) {
          // confirmed full or border
          if (grid[1][2] == 0 && grid[1][0] == 1) {
            // border
            System.out.print(18);
          } else {
            //checkerboard
            if(grid[1][0] == 0)
            {
              System.out.print(25);              
            }
            else// full board
              System.out.print(2);
          }
        } else {
          // plus
          System.out.print(15);
        }

      }

    }
    
}

