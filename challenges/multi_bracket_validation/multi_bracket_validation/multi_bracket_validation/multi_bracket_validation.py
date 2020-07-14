def multi_bracket_validation(input): 
    stack = [] 
  
    for bracket in input: 
        if bracket in ["(", "{", "["]: 
            stack.append(bracket) 
        else:  
            if not stack: 
                return False
            current_bracket = stack.pop() 
            if current_bracket == '(': 
                if bracket != ")": 
                    return False
            if current_bracket == '{': 
                if bracket != "}": 
                    return False
            if current_bracket == '[': 
                if bracket != "]": 
                    return False
    if stack: 
        return False
    return True


if __name__ == "__main__":
    input = "{()}[]"
    if multi_bracket_validation(input): 
        print("True")
    else : 
        print("False")

if __name__ == "__main__":
    input = "{)"
    if multi_bracket_validation(input): 
        print("True")
    else : 
        print("False")