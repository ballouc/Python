def checker(user):
    stack = []
    for character in user:
        if character == "(":
            stack.append(character)
        elif character == ")":
            if stack:
                stack.pop()
            else:
                print("no")
                return

# using the boolean operator of a list checks if the list is empty.
# if (list) returns TRUE if the list is [NOT] empty.
# if-elifs must be written backwards because of this.
    if stack:
        print("no")
    else:
        print("yes")


# if dunder name is dunder main :)
if __name__ == '__main__':
    s = "haha null"
    print("Parentheses balance checker. \nInput an expression with parentheses. Input an empty line when done.")
# Check each line until an empty line is given
    while s != "":
        s = input()
        if s != "":
            checker(s)
