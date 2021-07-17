code = input("Input brainfuck code here: ")
arr = [0] * 30000
i = 0  # pointer
begin_loop_index = 0  # keeps track of the most recent [
print()  # begin new line

x = 0  # index in code
while x < len(code):
    if code[x] == ">":
        i += 1
    elif code[x] == "<":
        i -= 1
    elif code[x] == "+":
        arr[i] += 1
    elif code[x] == "-":
        arr[i] -= 1
    elif code[x] == ".":
        print(chr(arr[i]), end='')
    elif code[x] == ",":
        arr[i] = ord(input()[0])  # only uses first char of input
    elif code[x] == "[":
        begin_loop_index = x
        if arr[i] == 0:
            while code[x] != "]":  # skip past the matching ]
                x += 1
    elif code[x] == "]":
        if arr[i] != 0:
            x = begin_loop_index - 1  # jump back to the matching [
    else:
        pass

    x += 1
