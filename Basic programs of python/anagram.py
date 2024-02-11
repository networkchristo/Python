def check(s1, s2):
    if sorted(s1) == sorted(s2):
        print("The strings are anagram")
    else:
        print("The strings are not anagram")

s1 = input("Enter the string 1 : ")
s2 = input("Enter the string 2 : ")

check(s1,s2)