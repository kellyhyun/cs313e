#  File: ExpressionTree.py

#  Description: This code creates and evaluates an expression tree. Also prints in prefix and postfix.

#  Student Name: Soomin Hyun

#  Student UT EID: sh52679

# Partner Name: Joon Kim (Unique Number: 52595)

# Partner UT EID: jk45873

# Course Name: CS 313E

# Unique Number: 52600

# Date Created: 11/11/21

# Date Last Modified: 11/12/21

import sys

operators = ['+', '-', '*', '/', '//', '%', '**']

class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append (data)

    def pop(self):
        if(not self.is_empty()):
            return self.stack.pop()
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0

class Node (object):
    def __init__ (self, data = None, lChild = None, rChild = None):
        self.data = data
        self.lChild = lChild
        self.rChild = rChild

    # printing statement to help me find the bugs
    def __str__(self):
        return (f"{self.data}")

    # gets the integer of the data
    def __int__(self):
        return(int(self.data))

class Tree (object):
    def __init__ (self):
        self.root = Node(None)
        # made an operator list to check if the current node we look at is an operator
        self.operatorlist = ['+', '-', '*', '/', '//', '%', '**']
    
    # this function takes in the input string expr and 
    # creates the expression tree
    def create_tree (self, expr):
        # start with the current as the root of the tree
        current = self.root
        # creat an empty stack where we will make the tree
        expr_stack = Stack()
        # split the expr string to have each number or operand or parenthesis be an individual token
        # this also takes out the spaces
        expr = expr.split()
        for token in expr:
            # all of these if else statements do what was specified in the assignment page
            # if we are starting a new expression:
            if token == '(':
                # makes the left child a node for the future data inputting
                current.lChild = Node(None)
                # puts the current node into the stack
                expr_stack.push(current)
                # makes sure that we put the next token's data into the left child
                current = current.lChild
            # if our current token is an operator:
            elif token in self.operatorlist:
                # make the nodes data as the current token
                current.data = token
                # makes the right child a token
                current.rChild = Node(None)
                # put the current token/node into the stack
                expr_stack.push(current)
                # we will put the next token's data into the right child
                current = current.rChild
            # if we are ending an expression
            elif token == ')':
                # if the stack isn't empty.. so the expression isn't done, pop the stack
                if not expr_stack.is_empty():
                    current = expr_stack.pop()
            # if the token is a number
            else:
                # make the data as a float so that the operators properly work always, and the end evaluation is a
                # float number. when printing prefix and postfix, this later gets fixed
                current.data = float(token)
                # pop the stack when inputting the number
                current = expr_stack.pop()

    # this function should evaluate the tree's expression
    # returns the value of the expression after being calculated
    def evaluate (self, aNode):
        # whenever the node is an operator, evaluate either side of the tree to then be able to evaluate the big tree
        if aNode.data in self.operatorlist:
            # recursively finds the value of each tree node
            result = self.operate(aNode.data, self.evaluate(aNode.lChild), self.evaluate(aNode.rChild))
            return result
        return aNode.data

    # function that calculates the result of the operators in the operator list
    # ['+', '-', '*', '/', '//', '%', '**']
    def operate (self, operator, first_operator, second_operand):
        if operator == '+':
            return first_operator + second_operand
        if operator == '-':
            return first_operator - second_operand
        if operator == '*':
            return first_operator * second_operand
        if operator == '/':
            return first_operator / second_operand
        if operator == '//':
            return first_operator // second_operand
        if operator == '%':
            return first_operator % second_operand
        if operator == '**':
            return first_operator ** second_operand

    # this function should generate the preorder notation of
    # the tree's expression
    # returns a string of the expression written in preorder notation
    def pre_order (self, aNode):
        result = ''
        result = self.pre_order_helper(aNode, result)
        return result

    # this function is a preorder helper to make it so that we can make the code recursive
    def pre_order_helper(self, aNode, result):
        if aNode != None:
            str_a_node = aNode
            # makes sure that if the node data was originally an int, it will turn it back into a float number
            if (aNode.data not in self.operatorlist) and (aNode.data//1 == aNode.data):
                str_a_node = int(aNode)
            additional_string = '{} '.format(str_a_node)
            result = additional_string
            # put the left children before the right children
            if aNode.lChild != None:
                result += self.pre_order_helper(aNode.lChild, result)
            if aNode.rChild != None:
                result += self.pre_order_helper(aNode.rChild, result)
        return result

    # this function should generate the postorder notation of 
    # the tree's expression
    # returns a string of the expression written in postorder notation
    def post_order (self, aNode):
        result = ''
        result = self.post_order_helper(aNode, result)
        return result

    # this function is like the preorder helper but it is in post order
    def post_order_helper(self, aNode, result):
        if aNode != None:
            str_a_node = aNode
            # makes sure that if the node data was originally an int, it will turn it back into a float number
            if (aNode.data not in self.operatorlist) and (aNode.data//1 == aNode.data):
                str_a_node = int(aNode)
            additional_string = '{} '.format(str_a_node)
            result = additional_string
            # put the left children before the right children still but also but the operand to the right of both.
            # making the additional string print after the original result but also making the right children go through
            # the recursive function first makes it print in the correct order.
            if aNode.rChild != None:
                result = self.post_order_helper(aNode.rChild, result) + result
            if aNode.lChild != None:
                result = self.post_order_helper(aNode.lChild, result) + result
        return result

# you should NOT need to touch main, everything should be handled for you
def main():
    # read infix expression
    line = sys.stdin.readline()
    expr = line.strip()
 
    tree = Tree()
    tree.create_tree(expr)

    # evaluate the expression and print the result
    print(expr, "=", str(tree.evaluate(tree.root)))

    # get the prefix version of the expression and print
    print("Prefix Expression:", tree.pre_order(tree.root).strip())

    # get the postfix version of the expression and print
    print("Postfix Expression:", tree.post_order(tree.root).strip())

if __name__ == "__main__":
    main()
