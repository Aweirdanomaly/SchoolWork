/*
 * Problem Set 1
 *
 * Practice with static methods, part I
 */

public class Methods {
    /*
     * printVertical - takes a string s and prints the characters of 
     * the string vertically -- with one character per line.
     */
    public static void printVertical(String s) {
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            System.out.println(c);
        }
    }
    /*
     * printWithSpaces - takes a string s and prints the characters of 
     * the string with spaces in between 
     */
    public static void printWithSpaces(String s) {
    for (int i = 0; i < s.length(); i++) {
        char c = s.charAt(i);
        System.out.print(c + " ");
    }
    }
    /*
     * middleChar - takes a string s and returns its middle character.
     * If the string has an even amount of characters, then the first middle character
     * is returned
     */
    
    public static char middleChar(String s) {
    	int x = s.length();
    	if (x % 2 == 0) {
    		char res = s.charAt(x/2-1);
    		return res;
    	}
    	else {
    		char res = s.charAt((x/2));
    		return res;
    	}
    }
    /*
     * moveToEnd - takes a string s and int i and returns a new string beggining from
     * i until the end of the original string plus the beginning until i concatenated at the end
     * of the string
     */
    public static String moveToEnd(String str, int i) {
    	if (i>str.length()) {
    		return str;
    	}
    	else {
    		String res = str.substring(0,i);
    		return str.substring(i) + res; 
    	}
    }
    
    public static void main(String[] args) {
        /* Sample test call */
        printVertical("method");     
        printWithSpaces("method");
        System.out.println(middleChar("Boston"));
        System.out.println(moveToEnd("Boston", 8));

    }

}
