# LAB EXERCISE 9

# Objective: In this lab, you will define three classes (Book, Library, PaperbackBook).
# PaperbackBook will inherit from the parent Book class. You will then create instances of
# the different kinds of books and add them to your "library".

class Book(): 
    """
    This is a class that contains information on Books.

    Attributes:
        title (str): The title of the book.
        author (str): The name of the author.

    """
    def __init__(self, title, author): 
        """
        The constructor of the <Book> class. Here you will need to create
        the instance variables that were described in the docstring above. 
        Note that the attributes are defined by parameters passed to this constructor method.
        
        Parameters:
            title (str): The title of the book.
            author (str): The name of the author.

        Returns:
            None
        """

        pass


    def __str__(self):
        """
        String method for the <Book> class. Whenever an instance of <Book> is passed to the 
        str() or print() functions, the string from this method will be returned.

        Parameters:
            None

        Returns:
            str: A string representation of <Book> instance in the format "<title> by <author>"
        """
        pass



class Library():
    """
    This is a class that contains information on a Library.

    Attributes:
        books (list): List of book instances in the library.
        torn_pages_tolerance (int): Number of torn pages a book can have and the library will still accept
        
   Methods (in addition to constructor and str):
        will_accept: Takes book instance as parameter and returns True or False is library will accept
        add_book: Takes book instance as parameter and adds it to list of books instance variable

    """
    def __init__(self):
        """
        The constructor of the <Library> class. Here you will need to create instance variables
        described in the docstring above. The Library constructor should take NO positional arguments, but
        set instance variables <books> to an empty list and <torn_pages_tolerance> to 3.
        
        Parameters:
            None

        Returns:
            None
        """

        pass


    def __str__(self):
        """
        String method for the <Library> class.

        Parameters:
            None

        Returns:
            str: A string representation of <Book> instance in the format:
                "This library contains <number of books> books"
                    
        """

        pass

    def will_accept(self, book):
        """
        Determines if the library will add a book instance to its collection
        depending on its conditions.

        if book instance is of PaperbackBook class:
            if the the num of torn pages is <= the library's torn page tolerance, return True.
            elif the num of torn pages is > the library's torn page tolerance, return False.
        else return True (else catches all plain book instances)
            HINT: there is a built-in isinstance() function to check what class an isntance
            came from

        Parameters:
            book: instance of any book class

        Returns:
            Boolean (True or False)
        """

        pass

    def add_book(self, book):
        """
        This method will modify the <books> attribute by appending the parameter <book>
        to it if the library will accept the book.
            HINT: call will_accept within this method to determine if book can be added

        Parameters:
            book: instance of any book class

        Returns:
            None
        """

        pass

class PaperbackBook(Book): # <- remember to fill in () for class inheritence!
    """
    This is a PaperbackBook class that inherits from the Book class. It will inherit
    all attributes and methods from Book. You will overwrite the parent constructor 
    to add an additional property but inherit the string method as is.

     Attributes:
        title (str): The title of the book.
        author (str): The name of the author.
        num_torn_pages (int): The number of torn pages in the PaperBook.
        
    Methods (in addition to constructor and str):
        rip_page: increases number of ripped pages by 1
    """

    def __init__(self, title, author):
        """
        The constructor of the <PaperbackBook> class. Here you will need to inherit the attributes 
        from the parent class, but add an additional instance variable <num_torn_pages> 
        and initialize it to 0. Note that the constructor takes two positional arguments, but will
        set three instance variables.
        
        Parameters:
            title (str): The title of the book.
            author (str): The name of the author.

        Returns:
            None
        """

        pass
 
    def rip_page(self):
        """
        This method will modify the <num_torn_pages> and increase it by one every time the
        method is called.

        Parameters:
            None

        Returns:
            None
        """
        pass
    
def main():

    # create an instance of Book class with title = "The Odyssey" and author = "Homer"
    # assign the instance to variable <homer_odyssey>
    homer_odyssey = None

    # print instance of book
    print(homer_odyssey)

    # create an instance of PaperbackBook class with title = "And Still I Rise" and author = "Maya Angelou"
    # assign the instance to varialbe <angelou_rise>
    angelou_rise = None

    # print instance of PaperbackBook
    print(angelou_rise)

    # create an instance of Library class and assign it to the variable <lib>
    lib = None

    # add book <homer_odyssey> to the library
    
    ### CODE HERE ###

    # increase <num_torn_pages> of book <angelou_rise> to 4 by calling <rip_page> method 4 times in a row.
    # Hint: you can do this using a for loop and the range() function
    # Note: each call increases <num_torn_pages> by 1.
   
    ### CODE HERE ###

    # set <torn_pages> equal to the number of torn pages of <angelou_rise>. Use the instance variable, do not hard code a number
    
    torn_pages = None

    # try to add <angelou_rise> to the library -- it shouldn't be added because the num_torn_pages is too high
    
    ### CODE HERE ###

    # print out the library's books -- there should be only one.
    
    ### CODE HERE ###

# END CODING HERE - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == '__main__':
    main()
