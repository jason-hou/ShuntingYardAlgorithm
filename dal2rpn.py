#coding=utf-8
'''convert Direct Algebraic Logic(DAL) to Reverse Polish Notation'''

__author__ = 'Jason Hou'

order = {'-':0, '+':0, '*':1, '/':1, '(':2, ')':2}

def convert(dal):
    '''convert dal to rpn'''
    output, stack = [], []
    def push(op):
        '''push op to stack'''
        if op==')':
            assert '(' in stack
            while(stack[-1]!='('):
                output.append(stack.pop())
            stack.pop()
        elif stack == [] or stack[-1] == '(' or order.get(stack[-1])<order.get(op):
            stack.append(op)
        elif stack[-1] != '(':
            output.append(stack.pop())
            push(op)
    assert dal.count('(') == dal.count(')'), 'parentheses not match'
    for i in dal.split():
        if i.isdigit():
            output.append(i)
        elif i in order:
            push(i)
        else:
            raise Exception('unknown operator:%s' % i)
    while(len(stack)):
        output.append(stack.pop())
    return ' '.join(i for i in output)

if __name__=='__main__':
    print(convert('1 + 2 * 3 + ( 2 * 4 + 3 ) * 2'))