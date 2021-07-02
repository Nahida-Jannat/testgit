# stack parenthesis Valid or Invalid

def parenthesis(open, close):
    if open == "(" and close == ")" :
        return True
    if open == "{" and close == "}" :
        return True
    if open == "[" and close == "]" :
        return "Valid"
    else:
        return "Invalid"

def valid_status(p):
    stack = []
    for i in range(len(p)):
        if p[i] == "(" or p[i] == "{" or p[i] == "[" :
            stack.append(p[i])
        
        elif p[i] == ")" or p[i] == "}" or p[i] == "]" :
            if parenthesis(stack[-1], p[i] or len(stack) != 0):
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return "Valid"
    else:
        return "Invalid"

p =input()
print(valid_status(p))