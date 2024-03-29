# p14220
p14220 ergasia eisagwgi stin epistimi twn upologistwn



class Stack:
    def init(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
exp = input('Please enter the line to check: ')
 
for c in exp:
    if c == '(':
        s.push(1)
    elif c == ')':
        if s.is_empty():
            is_balanced = False
            break
        s.pop()
else:
    if s.is_empty():
        is_balanced = True
    else:
        is_balanced = False
 
if is_balanced:
    print('Expression is correctly parenthesized.')
else:
    print('Expression is not correctly parenthesized.')
