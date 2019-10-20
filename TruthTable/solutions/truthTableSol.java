import java.util.Scanner;

public class truthTableSol {
    public static void main(String args[]) {
        Scanner keyboard = new Scanner(System.in);
        int numVariables = keyboard.nextInt();
        int rowNum = keyboard.nextInt();

        String binaryString = Integer.toBinaryString(rowNum);

        while(binaryString.replaceAll(" ", "").length() < numVariables)
        {
            binaryString = "F " + binaryString; 
        }

        binaryString = binaryString.replaceAll("1", "T ");
        binaryString = binaryString.replaceAll("0", "F ");

        System.out.println(binaryString);

        keyboard.close();
    }
}