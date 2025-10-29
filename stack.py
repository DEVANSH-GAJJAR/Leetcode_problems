class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Checks if the stack is empty."""
        return len(self.items) == 0

    def push(self, item):
        """Adds an item to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Removes and returns the top item from the stack.
        Raises an IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("Stack is empty, cannot pop.")
        return self.items.pop()

    def peek(self):
        """Returns the top item from the stack without removing it.
        Raises an IndexError if the stack is empty."""
        if self.is_empty():
            raise IndexError("Stack is empty, cannot peek.")
        return self.items[-1]

    def size(self):
        """Returns the number of items in the stack."""
        return len(self.items)

# Example usage:
if __name__ == "__main__":
    my_stack = Stack()

    print(f"Is stack empty? {my_stack.is_empty()}") 
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print(f"Stack size: {my_stack.size()}") 
    print(f"Top element: {my_stack.peek()}") 

    popped_item = my_stack.pop()
    print(f"Popped item: {popped_item}")
    print(f"Stack size after pop: {my_stack.size()}") 
    print(f"New top element: {my_stack.peek()}") 

    my_stack.pop()
    my_stack.pop()

    print(f"Is stack empty? {my_stack.is_empty()}") 
    try:
        my_stack.pop()
    except IndexError as e:
        print(f"Error: {e}") 
