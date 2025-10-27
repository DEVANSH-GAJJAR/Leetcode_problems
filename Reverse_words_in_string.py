def reverseWords(s):
    stack = []
    word = ""

    for ch in s:
        
        # If not a dot, build 
        # the current word
        if ch != '.':
            word += ch
        
        # If we see a dot, push 
        # the word into the stack
        elif word:
            stack.append(word)
            word = ""

    # Last word remaining, 
    # push it to stack
    if word:
        stack.append(word)

    # Rebuild the string from the stack
    return ".".join(stack[::-1])

if __name__ == "__main__":
    s = "..geeks..for.geeks."
    print(reverseWords(s))
