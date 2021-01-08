import sun.font.TrueTypeFont;

import java.util.LinkedList;
import java.util.Scanner;

/*

 * LLBag.java
 *
 *  Problem Set 6 Problem 6
 *
 *
 * Computer Science 112
 *
 *
 *   name: Jarar Zaidi
 *   email: jzaidi@bu.edu
 */
public class LLBag implements Bag {

        // Inner class for a node.  We use an inner class so that the LLList
        // methods can access the instance variables of the nodes.
        private class Node {
            private Object item;
            private Node next;

            private Node(Object i, Node n) {
                item = i;
                next = n;
            }
        }

        // fields of the LLList object
        private Node head;     // dummy head node
        private int length;    // # of items in the list

        /*
         * Constructs a LLList object for a list that is initially empty.
         */
        public LLBag() {
            head = new Node(null, null);
            length = 0;
        }

        /*
         * Constructs an LLList object containing the items in the specified array
         */
        public LLBag(Object[] initItems) {
            head = new Node(null, null);

            Node prevNode = head;
            for (int i = 0; i < initItems.length; i++) {
                Node nextNode = new Node(initItems[i], null);
                prevNode.next = nextNode;
                prevNode = nextNode;
            }

            length = initItems.length;
        }



        /*
     * toString - converts this ArrayBag into a string that can be printed.
     * Overrides the version of this method inherited from the Object class.
     */
    @Override
    public String toString(){

        String str = "{";

        // node to traverse
        Node trav = new Node(null,null);

        while (trav != null){
            // accumulate the string
            str += trav.item;

            // advance to next node
            trav = trav.next;

            str += ",";

        }

        str += "}";
        return str;

    }



    /*
     * remove - removes one occurrence of the specified item (if any)
     * from this ArrayBag.  Returns true on success and false if the
     * specified item (i.e., an object equal to item) is not in this ArrayBag.
     */
    public boolean remove(Object item) {

        return false;  // item not found
    }

    /*
     * add - adds the specified item to this ArrayBag. Returns true if there
     * is room to add it, and false otherwise.
     * Throws an IllegalArgumentException if the item is null.
     */
    public boolean add(Object item) {
        // ALWAYS Returns True b/c constrctor/LList doesnt need specify size
        return true;
    }


    /*
     * grab - returns a reference to a randomly chosen item in this ArrayBag.
     */
    public Object grab() {
        int whichOne = (int)(Math.random());
        int x = whichOne* this.numItems();
        Node trav = new Node(null,null);


        // generating a random index


        Node temp = this.head;

        // returning item at position randIndex

        for (int i = 0; i < x; i++) {

            temp = temp.next;

        }

        return temp.data;

    }

    /*
     * toArray - return an array containing the current contents of the bag
     */
    public Object[] toArray() {
        Object[] copy = new Object[3];

        return copy;
    }



    /*
     * contains - returns true if the specified item is in the Bag, and
     * false otherwise.
     */
    public boolean contains(Object item) {


        return false;
    }

    /*
     * numItems - accessor method that returns the number of items
     * in this ArrayBag.
     */
    public int numItems() {
        Node trav = new Node(null,null);

        int counter = 0;
        while (trav != null){
            trav = trav.next;
            counter++;
        }
        return counter;
    }



    /* Test the ArrayBag implementation. */
    public static void main(String[] args) {
        // Create a Scanner object for user input.
        Scanner scan = new Scanner(System.in);

        // Create an ArrayBag named bag1.
        System.out.print("number of items in bag 1: ");
        int numItems = scan.nextInt();
        Bag bag1 = new ArrayBag(numItems);
        scan.nextLine();    // consume the rest of the line

        // Read in strings, add them to bag1, and print out bag1.
        String itemStr;
        for (int i = 0; i < numItems; i++) {
            System.out.print("item " + i + ": ");
            itemStr = scan.nextLine();
            bag1.add(itemStr);
        }
        System.out.println("bag 1 = " + bag1);
        System.out.println();

        // Select a random item and print it.
        Object item = bag1.grab();
        System.out.println("grabbed " + item);
        System.out.println();

        // Iterate over the objects in bag1, printing them one per line.
        Object[] items = bag1.toArray();
        for (int i = 0; i < items.length; i++) {
            System.out.println(items[i]);
        }
        System.out.println();

        // Get an item to remove from bag1, remove it, and reprint the bag.
        System.out.print("item to remove: ");
        itemStr = scan.nextLine();
        if (bag1.contains(itemStr)) {
            bag1.remove(itemStr);
        }
        System.out.println("bag 1 = " + bag1);
        System.out.println();
    }

}
