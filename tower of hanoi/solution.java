import java.util.Scanner;

public class solution{

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        System.out.println("How many discs are on the tower?: ");
        int discs = input.nextInt();

        hanoi(discs, "A", "B", "C");
    }

    public static void move( String moveFrom, String moveTo){
        System.out.printf("Move disc from %s to %s!\n", moveFrom, moveTo);
    }

    public static void hanoi(int numOfDiscs, String moveFrom, String helper, String moveTo) {
        if (numOfDiscs == 0) { // Base Case
    
        } else { // solve remaining puzzle
            hanoi(numOfDiscs-1, moveFrom, moveTo, helper);
            move(moveFrom, moveTo);
            hanoi(numOfDiscs-1, helper, moveFrom, moveTo);
        }
    }
}