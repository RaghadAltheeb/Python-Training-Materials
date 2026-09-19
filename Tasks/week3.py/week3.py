#1
string = "Hello, World!"
print(string)

#2
def swap_case(s):       
    return s.swapcase()  #switching the case of the characters in "s" (uppercase to lowercase and vice versa) and store the input in (result).
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)



#3
def split_and_join(line):
    
    w=line.split(" ")     #separated the words between each space.
    return "-" .join(w)   #connected each word with a "-"
   
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#4?
def print_full_name(first, last):
    print("Hello",first,last,"! You just delved into python.")
    #print(f"Hello {first} {last}! You just delved into python.")
if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)