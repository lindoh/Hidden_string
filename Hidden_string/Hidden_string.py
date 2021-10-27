#To find a short hidden string inside a longer string

#Hidden string function definition
def hidden_str(string, sub_string):
    size = len(sub_string)
    start = 0    #Start index for the find() method

    #Iterate through the sub-string to find the hidden word from the string
    for char in sub_string:
        start = string.find(char, start)

        if start == -1:     #If the character is not found, break 
            break
        else:               #Else, decrement the sub_string size until 0
            size -= 1

        if size == 0:       #Done iterating through sub-string without breaking out of the loop
            print('Yes')    #Yes, we found the hidden string
    if size > 0:            
        print('No')         #No, we didn't find the hidden string

#--------------------------Sample Tests-----------------------------------------------------
string = "vcxzxduybfdsobywuefgas"
sub_string = "dog"
hidden_str(string, sub_string)
print()

string = "vcxzxdcybfdstbywuefsas"
sub_string = "dog"
hidden_str(string, sub_string)
print()

string = "Nabucodonosor"
sub_string = "donor"
hidden_str(string, sub_string)
print()

string = "Nabucodonosor"
sub_string = "donut"
hidden_str(string, sub_string)
print()