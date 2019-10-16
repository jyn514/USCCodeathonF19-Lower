import java.util.Scanner;

public class IceSlideSol {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        int gridDimX = keyboard.nextInt();
        int gridDimY = keyboard.nextInt();
        int energy = keyboard.nextInt();
        String dummy = keyboard.nextLine();

        int curPosX = 0;
        int curPosY = 0;
        String[][] board = new String[gridDimY][gridDimX];
        String curLine = "";
        for (int y = 0; y < gridDimY; y++) {
            curLine = keyboard.nextLine();
            for (int x = 0; x < gridDimX; x++) {
                board[y][x] = curLine.substring(x, x + 1);
                if (board[y][x].equals("2")) {
                    curPosX = x;
                    curPosY = y;
                }
            }
        }
        String curDirection = "";
        while (true) {
            curDirection = keyboard.nextLine();
            if (curDirection.equals("Stop") || energy == 0) {
                break;
            }
            if (curDirection.equals("up")) {
                while (curPosY - 1 >= 0 && !board[curPosY - 1][curPosX].equals("1") && energy > 0) {
                    board[curPosY][curPosX] = "0";
                    curPosY -= 1;

                    energy -= 1;
                    char curTile = board[curPosY][curPosX].charAt(0);
                    int letterAsInt = Character.getNumericValue(curTile);

                    if (letterAsInt > 9) {
                        energy += (letterAsInt - 9);
                    }
                    if (energy > 30) {
                        energy = 30;
                    }
                    board[curPosY][curPosX] = "2";
                }
            }
            if (curDirection.equals("right")) {
                while (curPosX + 1 < gridDimX && !board[curPosY][curPosX + 1].equals("1") && energy > 0) {
                    board[curPosY][curPosX] = "0";
                    curPosX += 1;

                    energy -= 1;
                    char curTile = board[curPosY][curPosX].charAt(0);

                    int letterAsInt = Character.getNumericValue(curTile);

                    if (letterAsInt > 9) {
                        energy += (letterAsInt - 9);
                    }
                    if (energy > 30) {
                        energy = 30;
                    }
                    board[curPosY][curPosX] = "2";

                }
            }
            if (curDirection.equals("down")) {
                while (curPosY + 1 < gridDimY && !board[curPosY + 1][curPosX].equals("1") && energy > 0) {
                    board[curPosY][curPosX] = "0";
                    curPosY += 1;

                    energy -= 1;
                    char curTile = board[curPosY][curPosX].charAt(0);

                    int letterAsInt = Character.getNumericValue(curTile);

                    if (letterAsInt > 9) {
                        energy += (letterAsInt - 9);
                    }
                    if (energy > 30) {
                        energy = 30;
                    }
                    board[curPosY][curPosX] = "2";

                }
            }

            if (curDirection.equals("left")) {
                while (curPosX - 1 >= 0 && !board[curPosY][curPosX - 1].equals("1") && energy > 0) {
                    board[curPosY][curPosX] = "0";
                    curPosX -= 1;

                    energy -= 1;
                    char curTile = board[curPosY][curPosX].charAt(0);

                    int letterAsInt = Character.getNumericValue(curTile);

                    if (letterAsInt > 9) {
                        energy += (letterAsInt - 9);
                    }
                    if (energy > 30) {
                        energy = 30;
                    }
                    board[curPosY][curPosX] = "2";

                }
            }
            // System.out.println(curDirection);

            // System.out.println("```");

            // for (int y = 0; y < gridDimY; y++) {
            //     for (int x = 0; x < gridDimX; x++) {
            //         System.out.print(board[y][x]);
            //     }
            //     System.out.println();
            // }
            // System.out.println("```");

            // System.out.println("energy: " + energy + "\n");

        }

        keyboard.close();
        System.out.println(curPosX + " " + curPosY + " " + energy);
    }

}