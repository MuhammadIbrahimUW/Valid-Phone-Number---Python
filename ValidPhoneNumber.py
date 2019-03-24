## Valid Phone Number Checker

def num_only():
    '''
    returns the user inputed phone number in the form of only ten digits, and
    prints the string 'Thanks!' if the number is inputted in a correct format
    or prints the string 'Invalid number.' if the input is not in correct form
    
    num_only: None -> Str
    
    examples:
    >>> num_only()
        Enter a phone number:(519)888-4567
        Thanks!
        '5198884567'
    >>> num_only()
        Enter a phone number:90512345678
        Invalid number.
    '''
    
    s = input("Enter a phone number:")

    
    if str.isdigit(s) == True and len(s) == 10:
        print('Thanks!')
        return(s)
        
    elif str.isdigit(s[:3]) == True and s[3:4] == "-" and \
         str.isdigit(s[4:7]) == True and s[7:8] == "-" and \
         str.isdigit(s[8:12]) == True and len(s) == 12:
        print('Thanks!')
        return(s[:3] + s[4:7] + s[8:12])
        
        
    elif s[:1] == "(":
        if len(s) == 12 and str.isdigit(s[1:4]) == True and \
           s[4:5] == ")" and str.isdigit(s[5:12]) == True:
            print('Thanks!')
            return(s[1:4] + s[5:12])
        
        if len(s) == 13 and str.isdigit(s[1:4]) == True and \
           s[4:5] == ")" and str.isdigit(s[5:8]) == True and \
           s[8:9] == "-" and str.isdigit(s[9:13]) == True:
            print('Thanks!')
            return(s[1:4] + s[5:8] + s[9:13])
            
        else:
            print('Invalid number.')
    
    else:
        print('Invalid number.')