def add_chocolate(shopping_list: list):
    """My housemate is a real health-nut, but I like chocolate. This function 
    adds the string "chocolate" to any list it receives, and returns the 
    modified list. That way our shopping list is always correct.

    Arguments:
        - shopping_list: a list of strings

    Returns:
        - the same list, with the string "chocolate" added to the end
    """
    # chocolate_list = shopping_list.append(add_chocolate)
    # print(chocolate_list)

    # Modified in place do not need to reassign, jut return
    shopping_list.append("chocolate")
    return shopping_list


def lou_bega(lyrics_list: list):
    """This function accepts a list of strings and adds the words 
    "A little bit of " to the front of each.
    
    Arguments:
        - lyrics_list: a list of strings
    
    Returns:
        - the same list, but each string now has "A little bit of " 
        prepended to it.

    Example input: 
        [
            "Monica in my life", 
            "Erica by my side", 
            "Rita's all I need"
        ]
        
    Example output: 
        [
            "A little bit of Monica in my life", 
            "A little bit of Erica by my side", 
            "A little bit of Rita's all I need"
        ]
    """
    
    new_lyrics = []
    prefix_to_add = "A little bit of "

    for lyric in lyrics_list:
        new_lyrics.append(prefix_to_add + lyric)

    return new_lyrics

# This is how I can test it and then run this file 

# lyrics = [
#             "Monica in my life", 
#             "Erica by my side", 
#             "Rita's all I need"
#         ]
# print(lou_bega(lyrics))

# Another way to do this is to use f strings - check the screenshot in photos 


    

def assemble_guest_list():
    """This function repeatedly prompts the user for the name of a dinner guest.
    Each string the user supplies is added to a list. If/when the user hits 
    "Enter" without typing anything, the function stops asking and 
    returns the list.
    
    Arguments: None!
    
    Returns:
        - a list of strings supplied by the user
    """
    # Make a list to put things in
    guest_list = []
    # Prompt the user to enter a name
    guest_name = input("Enter guest's name: ")
    # If the input is not empty, which means users have entered something
    while guest_name != "":
        # Add the user input (guest_name) to the list (guest_list)
        guest_list.append(guest_name)
        # And then prompt user to add a name again 
        guest_name = input("Enter guest's name: ")
    # If not, which means if it is an empty string:
    # Which means if the users just pressed enter - return the guest list
    return(guest_list)

# To run this function 
# print(assemble_guest_list())
# Check Reece's alternative in photos

def is_prime(some_number: int): # A bit trickier!
    """This function tests to see if the input is a prime number.
    Whenever a prime number is divided by an integer larger than 1 and smaller
    than itself, the result includes a remainder.

    NOTE: The lowest prime number is 2. 1 and 0 are not prime.
    
    Arguments:
        - some_number: an integer to be tested for prime-ness

    Returns:
        - a boolean representing whether or not some_number is prime
    """

    # This function has an argument int which means that it expects an input 
    # Does that mean we do not prompt the user?
    # Divide the input integer by numbers larger than 1 and smaller than itself 
    # If it includes a remainder - it is a prime number 
    # Then we also need to check if the number is lower than 2, if it is, then automatically
    # it is not a prime number 
    # The prime numbers are = 2,3,5,7,11
    # We can check if the number is in the range (2 to 12) and then the conditions 
    
    if some_number <2:
        return False
    if some_number == 2:
        return True  

# Get the divisors and iterate over them
    for i in range(2,some_number):
        # If some_number is not divisible by i, it is a prime number
        if some_number % i != 0: 
            return True 
    
    # Else it is
    return True




    # if some_number < 2:
    #     return False 
    # elif some_number % 2 == 0:
    #     return False 
    # elif some_number % some_number-1 ==0:
    #     return False
    # else:
    #     return True
    
    # Hint
    #   int(1.5) == 1.0

