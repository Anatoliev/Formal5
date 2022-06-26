rules = {
    "S": ("aBS", "cfBC", "aS", "cfc"),
    "A": ("bA", "b"),
    "B": ("A"),
    "C": ("c")
}
shifts = {
    "B": ("S", "C", "a", "c"),
    "a": ("S", "B", "A", "a", "c", "b"),
    "b": ("f"),
    "c": ("B", "A", "c", "b"),
    "f": ("A", "b")
}
convolution = {
    "A": ("S", "C", "a", "c"),
    "f": ("S", "C", "a", "c")
}

def find_terminal(char: str):
    char = ''.join(i for i in char)
    for keys, values in rules.items():
        for value in values:
            if value == char:
                return keys
    return None

def check_input(string: str):
    stack = ["#"]
    prev = ''
    cnt = 0
    if not string[-1] == "#":
        string.join("#")
    while stack != ["#", "S"]:
        print(f"String: {string:<15}Stack: {stack}")
        prev = string
        if stack == ["#"]:
            stack.append(string[0])
            string = string[1:]
            continue
        else:
            values = shifts.get(stack[-1])
            if len(string) != 0 and string[0] in values:
                stack.append(string[0])
                string = string[1:]
                continue
            else:
                values = convolution.get(stack[-1])
                if len(string) != 0 and string[0] in values:
                    for idx in range(len(stack)):
                        res = find_terminal(stack[-idx:])
                        if res:
                            stack = stack[:(len(stack)-len(stack[-idx:]))]
                            stack.append(res)
                            continue
                else:
                    if len(string) == 0:
                        for idx in range(len(stack)):
                            res = find_terminal(stack[-idx:])
                            if res:
                                stack = stack[:(len(stack)-len(stack[-idx:]))]
                                stack.append(res)
                                continue
                    else:
                        return False
    return True


if __name__ == '__main__':
    string = input()
    print(check_input(string))
