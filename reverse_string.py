#make a reverse string
string_testing = "Hi I´m some string"

def reverse_string(some_string):
    if type(some_string) == str:
        return some_string[::-1]
    else:
        return "not a string"    

print(reverse_string(string_testing))   
print(reverse_string(1))     
