/*
 * Problem Set 2
 *
 * Array-processing methods, part II
 */
import java.util.*;
public class ArrayMethods {
	public static final String[] DAYS = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
	
 public static void main(String[] args) {
	 
	 int[] arr = {1, 2, 3, 3, 8, 8, 8, 8, 11, 11, 11, 14, 19, 19};
	 System.out.println(mostFrequentValue(arr));
}
 /// takes in a String "day" and returns its position in the array DAYS
 public static int getDayIndex(String day) {
	 day = day.substring(0,1).toUpperCase() + day.substring(1).toLowerCase();
	 for (int i = 0; i < DAYS.length;i++) {
		 if (DAYS[i].contentEquals(day)) {
			 return i;
		 }
	 }
	 return -1;
 }
 
 /// takes in an array "values" and swaps the position of every pair of elements in it
 /// Nothing is returned
 public static void swapAdjacent(int[] values) {
	 if (values == null) {
		 throw new IllegalArgumentException("Array values are null");
	 }
	 int l = values.length - 1;
	 int o;
	 if (values.length % 2 == 0) {
	  l = values.length;
	 }

	 for(int i = 0;i < l; i += 2) {
		 o = values[i]; 
		 values[i] = values[i+1];
		 values[i+1] = o;
	 }
	 
 }
 /// takes in array "values" and int 'cap" and creates and returns a
 /// new array where the values greater than cap are changed into cap
 public static int[] copyCapped(int[] values, int cap) {
	 if (values == null) {
		 throw new IllegalArgumentException("Array values are null");
	 }
	 int[] res = new int[values.length]; 
	 for (int i = 0;i<values.length;i++) {
		 if (values[i]<cap) {
			 res[i] = values[i];
		 }
		 else {
			 res[i] = cap;
			 }
		 }
	 return res;
	 }
///takes in a sorted int array "arr" and returns the most frequent value in the array
 public static int mostFrequentValue(int[] arr) {
	 if (arr == null || arr.length == 0) {
		 throw new IllegalArgumentException("Array values are null");
	 }
	 int w = arr[0];
	 int count = 0;
	 int fin = 0;
	 int ans = arr[0];
	 for (int i = 0; i<arr.length;i++) {
		  
		 if (arr[i] == w) {
			 count += 1;	 
		 }
		 else {
			 w = arr[i];
			 count = 0;
		 }
		 if (count > fin) {
			 ans = w;
			 fin = count;
		 }
	 }
	 return ans;
	 
 }
 ///takes in two int arrays "arr1" & "arr2" and returns the index where "arr1" occurs in "arr2"
 public static int indexOf(int[] arr1, int[] arr2) {
	 if (arr1 == null || arr1.length == 0 || arr2 == null || arr2.length == 0) {
		 throw new IllegalArgumentException("Array values are null");
	 }
	 for (int i = 0; i<arr2.length;i++) {
		 if(arr1[0] == arr2[i] ) {
			 if (arr1[1] == arr2[i+1]) {
				 if (arr1[2] == arr2[i+2]) {
				 return i;
			 }
		 }
	 }
 }
	 return -1;
 }
}