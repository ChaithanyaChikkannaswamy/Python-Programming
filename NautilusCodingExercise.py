##Question:
##    Improve the following code for:
##        ● Style
##        ● Simplicity
##        ● Maintainability
##
##
##        def f():
##            if A:
##                z()
##                if B:
##                    y()
##                    if C:
##                        x()
##                        if D:
##                            w()
##                            return True
##                        else:
##                            v()
##                            return False
##                    else:
##                        u()
##                        return False
##                else:
##                    t()
##                    return False
##            else:
##                s()
##                return False
##
##
##Date: May 20th 2021
##
##Solution:
##    Using nested if-else block has certain disadvantages like:
##    * When the number of conditions in the nested if-else block increases, the program maintaiance complexity also increases.
##    * Nested if-else block makes it difficlut to test and debug the program.
##    * Complex program structure.
##
##    To over come the above disadvantages we can optimize the code in simple and easy to maintain way as given below.
##    Here, instead of using nested if-else block, we can use a single boolean variable which can check of various conditions
##    and execute the block of code accordingly.
##    
   
def f():
    # assign a boolean variable to the first if condition
    bool valid = A
    # first if block will be executed as we have assigned the valid variable to 'A'
    if valid:
        z()
        return True
    # execute the else part of the block
    s()
    return False

    # update the valid variable such that if check for both A and B using && operator
    valid = valid && B
    if valid:
        y()
        return True
    # execute the else part of the block
    t()
    return False

    # update the valid variable such that if check for both A, B and C using && operator
    valid = valid && C
    if valid:
        x()
        return True
    # execute the else part of the block    
    u()
    return False

    # update the valid variable such that if check for both A, B, C and D using && operator
    valid = valid && D
    if valid:
        w()
        return True
    # execute the else part of the block    
    v()
    return False




