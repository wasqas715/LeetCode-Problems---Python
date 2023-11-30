# This can be cleaned up if an equation is setup rather than by n / 26
def converttotitle(columnNumber):
        first = divmod(columnNumber- 1, 26)
        y = first[0]
        if first[0] == 0:
              z = chr(97 + first[1]).upper()
              return z
        
        elif first[0] <= 26:
            y = chr(96 + first[0]).upper()
            z = chr(97 + first[1]).upper()
            return(f'{y}{z}')
        
        elif first[0] <= 676:
            second = divmod(y, 26)
            x = chr(96 + second[0]).upper()
            y = chr(96 + second[1]).upper()
            z = chr(97 + first[1]).upper()
            return(f'{x}{y}{z}')
        
        elif first[0] < 17576:
             second = divmod(y, 26)
             third = divmod(second[0],26)
             w = chr(96 + third[0]).upper()
             x = chr(96 + third[1]).upper()
             y = chr(96 + second[1]).upper()
             z = chr(97 + first[1]).upper()
             return(f'{w}{x}{y}{z}') 
        
        elif first[0] <= 456976:
             second = divmod(y-1, 26)
             third = divmod(second[0],26)
             fourth = divmod(third[0],26)
             v = chr(96 + fourth[0]).upper()
             w = chr(96 + fourth[1]).upper()
             x = chr(96 + third[1]).upper()
             y = chr(97 + second[1]).upper()
             z = chr(97 + first[1]).upper()
             print(second)
             print(third)
             print(fourth)
             return(f'{v}{w}{x}{y}{z}') 
        
        elif first[0] <= 11881376:
             second = divmod(y, 26)
             third = divmod(second[0],26)
             fourth = divmod(third[0],26)
             fifth = divmod(fourth[0],26)
             u = chr(96 + fifth[0]).upper()
             v = chr(96 + fifth[1]).upper()
             w = chr(96 + fourth[1]).upper()
             x = chr(96 + third[1]).upper()
             y = chr(96 + second[1]).upper()
             z = chr(97 + first[1]).upper()
             return(f'{u}{v}{w}{x}{y}{z}') 
        
        elif first[0] <= 308915776:
             second = divmod(y, 26)
             third = divmod(second[0],26)
             fourth = divmod(third[0],26)
             fifth = divmod(fourth[0],26)
             sixth = divmod(fifth[0],26)
             t = chr(96 + sixth[0]).upper()
             u = chr(96 + sixth[1]).upper()
             v = chr(96 + fifth[1]).upper()
             w = chr(96 + fourth[1]).upper()
             x = chr(96 + third[1]).upper()
             y = chr(96 + second[1]).upper()
             z = chr(97 + first[1]).upper()
             return(f'{t}{u}{v}{w}{x}{y}{z}') 
        
x = 5473578
print(converttotitle(x))

y = chr(96 + 25).upper()
print(y)