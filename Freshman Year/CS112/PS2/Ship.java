/*
 * Problem Set 2
 *
 * Battleship-Blueprint class for Ship objects, part II
 */
public class Ship {
	private String type;
	private int length;
	private int numHits;

///takes in String "type" and int "length" and builds object of type Ship. Nothing is returned.
public Ship(String type, int length) {
	if (type == null ||type == "" || length < 1) {
		throw new IllegalArgumentException("Either type or length is wack");
	}
	this.type = type;
	this.length = length;
	numHits = 0;
}
///The following methods all get a variable from the class Ship and return it
///No inputs, returns String "type" 
public String getType() {return type;}
///No inputs, returns int "length" 
public int getLength() {return length;}
///No inputs, returns int "numHits" 
public int getNumHits() {return numHits;}
///No inputs, returns the first character of "type" as a char 
public char getSymbol() {return type.charAt(0);}

///takes in no parameters and increases int "numHits" by 1
public void applyHit() {
	numHits += 1;
}
///takes in no parameters and returns whether a ship has been sunk as a boolean
public boolean isSunk() {
	if (numHits >= length) {
		return true;
	}
	return false;
}
///takes in no parameters and returns the String form of the object written as ("type" of length "length")
public String toString() {
	return (type + " of length " + length);
}



}
