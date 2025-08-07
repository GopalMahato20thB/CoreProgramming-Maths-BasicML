"""
Given a valid IPv4 address address, return a defanged version of that IP address.

A defanged IP address replaces every "." with "[.]".

Example 1:
Input: address = "1.1.1.1"
Output: "1[.]1[.]1[.]1"

Example 2:
Input: address = "255.100.50.0"
Output: "255[.]100[.]50[.]0"

"""
def transform_defang(ip):
    defang_form = ""
    for i in ip:
        if i == ".":
            i = "[.]"
        defang_form += i
    return defang_form     
print(transform_defang("255.100.50.0"))

### using python's replace function 

def transform_defang(ip):
    return ip.replace(".", "[.]")
print(transform_defang("255.100.50.0"))


        
