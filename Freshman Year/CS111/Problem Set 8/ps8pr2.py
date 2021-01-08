#
# ps8pr2.py  (Problem Set 8, Problem 2)
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
#### Put your code for problem 2 below. ####
    def advance_one(self):
        """ takes in object 'date' and moves it forward one day"""
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() == True and self.month == 2 and self.day == 28:
                self.day += 1
        else:
            if self.day >= days_in_month[self.month]:
                self.day = 1
                if self.month == 12:
                    self.month = 1
                    self.year += 1
                else:
                    self.month += 1     
            else:
                self.day += 1

    def advance_n(self, n):
        """ takes in object 'date' and integer 'n' and moves 'date' forward
        'n' days while printing all the 'dates' in between; endpoint inclusive """
        if n == 0:
            print(self)
        else:
            i = 0
            while i < n:
                print(self)
                self.advance_one()
                i += 1
            print(self)
            
    def __eq__(self, other):
        """ checks if the dates of 'self' and 'other' are equal """
        if self.month == other.month and self.day == other.day and self.year == other.year:
            return True
        else:
            return False 
        
    def is_before(self, other):
        """ takes in objects 'self' and 'other' and returs True if the date of
        'self' happens before the date of 'other' otherwise it returns False """
        if self.year < other.year:
            return True
        elif self.month < other.month and self.year == other.year:
            return True
        elif self.day < other.day and self.month == other.month and self.year == other.year:
            return True
        else:
            return False
        
    def is_after(self, other):
        """ takes in objects 'self' and 'other' and returs True if the date of
        'self' happens after the date of 'other' otherwise it returns False """
        if self.is_before(other) == True:
            return False
        elif self == other:
            return False
        else:
            return True

    def days_between(self, other):
        """ takes in two Date objects 'self' and 'other' and returns the amount
        of days between them """  
        count = 0
        sc = self.copy()
        oc = other.copy()
        if sc.is_after(oc) == True:
            while sc != oc :
                oc.advance_one()
                count += 1
            return count
        else:
            while oc != sc :
                sc.advance_one()
                count -= 1
            return count
    
    def day_name(self):
        """ takes in a date object 'self' and returns what day of the week
        it was on that date"""
        std = Date(11, 11, 2019)
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        days = self.days_between(std)
        index = days % 7
        return day_names[index]
        
                
                