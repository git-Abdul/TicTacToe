package Project;
import java.util.*;
class TicTacToe {
    void PrintArray(char [][] box) {
        for(int i = 0; i<3; i++) {
            for(int j = 0; j<3; j++) {
                char ch = box[i][j];
                if(ch == ' ') {
                    System.out.print("' "+"  ");
                }
                else {
                    System.out.print(box[i][j]+"   ");
                }
            }
            System.out.println();
        }
    }
    void checkWinner(char ch, char [][] box) {
        TicTacToe ob = new TicTacToe();
        for(int i = 0; i<3; i++) {
            // Checking rows:
            if(box[i][0] == box[i][1] && box[i][0] == box[i][2] && box[i][0] == ch) {
                System.out.println("==============================================================");
                System.out.println();
                ob.PrintArray(box);
                System.out.println();
                System.out.println("Player " + (ch == 'O' ? "1" : "2") + " wins!");
                System.out.println();
                System.out.println("==============================================================");
                System.out.println();
                System.exit(0);
            }
            // Checking columns:
            else if(box[0][i] == box[1][i] && box[0][i] == box[2][i] && box[0][i] == ch) {
                System.out.println("==============================================================");
                System.out.println();
                ob.PrintArray(box);
                System.out.println();
                System.out.println("Player " + (ch == 'O' ? "1" : "2") + " wins!");
                System.out.println();
                System.out.println("==============================================================");
                System.out.println();
                System.exit(0);
            }
        }
        // Checking right diagonal:
        if(box[0][0] == box[1][1] && box[0][0] == box[2][2] && box[0][0] == ch) {
            System.out.println("==============================================================");
            System.out.println();
            ob.PrintArray(box);
            System.out.println();
            System.out.println("Player " + (ch == 'O' ? "1" : "2") + " wins!");
            System.out.println();
            System.out.println("==============================================================");
            System.out.println();
            System.exit(0);
        }
        // Checking left diagonal:
        else if(box[0][2] == box[1][1] && box[0][2] == box[2][0] && box[0][2] == ch) {
            System.out.println("==============================================================");
            System.out.println();
            ob.PrintArray(box);
            System.out.println();
            System.out.println("Player " + (ch == 'O' ? "1" : "2") + " wins!");
            System.out.println();
            System.out.println("==============================================================");
            System.out.println();
            System.exit(0);
        }
    }
    boolean checkValidMove(char [][] box, int r, int c) {
        if(r>3 || c>3 || box[r-1][c-1] != ' '){
            return false;
        }
        return true;
    }
    public static void main(String args[]) { 
        Scanner sc = new Scanner(System.in);
        char box[][] = new char[3][3];
        int m = 0;
        TicTacToe ob = new TicTacToe();
        // Declaring array values:
        for(int i = 0; i<3; i++) {
            for(int j = 0; j<3; j++) {
                box[i][j] = ' ';
            }
        }
        // Game loop:
        while(true) {
            if(m!=9) {
                if(m!=9) {
                    System.out.println("Player 1: Enter row and column number");
                    String clm = "";
                    String row = "";
                    String input1 = sc.next();
                    row += input1.charAt(0);
                    clm += input1.charAt(2);
                    int p1r = Integer.valueOf(row);
                    int p1c = Integer.valueOf(clm);
                    if(ob.checkValidMove(box, p1r, p1c) == false) {
                        System.out.println("Invalid Input");
                        sc.close();
                        System.exit(0);
                    }
                    box[p1r-1][p1c-1] = 'O';
                    System.out.println();
                    ob.PrintArray(box);
                    System.out.println();

                    ob.checkWinner('O', box);
                    ob.checkWinner('X', box);

                    m++;
                    clm = "";
                    row = "";
                }
                if(m!=9) {
                    System.out.println("Player 2: Enter row and column number");
                    String clm2 = "";
                    String row2 = "";
                    String input2 = sc.next();
                    row2 += input2.charAt(0);
                    clm2 += input2.charAt(2);
                    int p2r = Integer.valueOf(row2);
                    int p2c = Integer.valueOf(clm2);
                    if(ob.checkValidMove(box, p2r, p2c) == false) {
                        System.out.println("Invalid Input");
                        System.exit(0);
                    }
                    box[p2r-1][p2c-1] = 'X';
                    System.out.println();
                    ob.PrintArray(box);
                    System.out.println();
                    System.out.println("==============================================================");
                    System.out.println();

                    ob.checkWinner('O', box);
                    ob.checkWinner('X', box);

                    m++;
                    clm2 = "";
                    row2 = "";
                }
            }
            else if(m == 9) {
                System.out.println();
                System.out.println("Both players have tied.");
                System.out.println("==============================================================");
                System.out.println();
                System.exit(0);
            }
        }
    }
}
