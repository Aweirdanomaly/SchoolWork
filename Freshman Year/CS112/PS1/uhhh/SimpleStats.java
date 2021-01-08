/*
 * Problem Set 1
 * 
 * A simple interactive program that performs operations 
 * on a set of three integers.
 */

import java.util.*;

public class SimpleStats {

    public static void printMenu() {
        System.out.println("(0) Enter new numbers");
        System.out.println("(1) Find the largest");
        System.out.println("(2) Compute the sum");
        System.out.println("(3) Compute the range (largest - smallest)");
        System.out.println("(4) Compute the average");
        System.out.println("(5) Print the numbers in ascending order");
        System.out.println("(6) Quit");
        System.out.println();
    }
    
    /*** PUT YOUR SEPARATE HELPER METHODS FOR OPTIONS 1-5 HERE ***/
    
    
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);        

        // the three integers
        int n1 = 2;
        int n2 = 4;
        int n3 = 6;

        boolean more_input = true;
        
        do {
            System.out.print("The current numbers are: ");
            System.out.println(n1 + " " + n2 + " " + n3);
            
            printMenu();
            System.out.print("Enter your choice: ");
            int choice = scan.nextInt();
            
            /*
             * Expand this conditional statement to process choices 1-5.
             * Make sure to follow the guidelines in the assignment for
             * doing so.
             */
            if (choice == 0) {
                System.out.print("Enter three new numbers: ");
                n1 = scan.nextInt();
                n2 = scan.nextInt();
                n3 = scan.nextInt();
            } else if (choice == 6) {
                more_input = false;
            } 
            else if (choice == 1) {
            	System.out.println("The largest of the numbers is " + Max(n1, n2, n3));
            }
            else if (choice == 2) {
            	System.out.println("The sum of the numbers is " + Sum(n1, n2, n3));
            }
            else if (choice == 3) {
            	System.out.println("The range of the numbers is " + Range(n1, n2, n3));
            }
            else if (choice == 4) {
            	System.out.println("The average of the numbers is " + Average(n1, n2, n3));
            }
            else if (choice == 5) {
            	 MinToMax(n1, n2, n3);
            }
            else {
                System.out.println("Invalid choice. Please try again.");
            }
            
            System.out.println();
        } while (more_input);
        
        System.out.println("Have a nice day!");
    }
    /*
     * Max - Takes in int n1, int n2, and int n3 and returns the biggest int
     */
    public static int Max(int n1, int n2, int n3 ) {
    	int ans = Math.max(n3, Math.max(n1,n2));
    	return ans;
    }
    /*
     * Sum - Takes in int n1, int n2, and int n3 and returns their sum
     */
    public static int Sum(int n1, int n2, int n3 ) {
    	return n1 + n2 + n3;
    }
    /*
     * Range - Takes in int n1, int n2, and int n3 and returns their range
     */
    public static int Range(int n1, int n2, int n3 ) {
    	int max = Max(n1, n2, n3);
    	int min = Math.min(n1, Math.min(n2, n3));
    	return max - min;
    }
    /*
     * Average - Takes in int n1, int n2, and int n3 and returns their average
     */
    public static float Average(int n1, int n2, int n3 ) {
    	return (Sum(n1,n2,n3)/3.0f);
    }
    /*
     * MinToMax - Takes in int n1, int n2, and int n3 and returns them in increasing 
     * order
     */
    public static void MinToMax(int n1, int n2, int n3) {
    	int x = Math.min(n1, Math.min(n2, n3));
    	int z = Max(n1,n2,n3);
    	int y = 0;
    	if (x != n1 && z != n1) {
    		 y = n1;
    	}
    	else if (x != n2 && z != n2) {
    		 y = n2;
    	}
    	else {
    		 y = n3;
    	}
    	
    	System.out.println("In order, the numbers are: " + x + " " + y + " " + z );
    	
    	
    }
}
