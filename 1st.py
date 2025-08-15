import sys

class node():
    def __init__(self, action, parent, state):
        self.state= state
        self.action= action
        self.parent= parent

class stackfrontier():
    def __init__(self):
        self.frontier = []  #creating a stack frontier

    def add(self, node):
        self.frontier.append(node)       # appending/adding a new node
    
    def contain_state(self, state):
        return any( node.state ==state for node in self.frontier)
    
    def empty(self):
        return    len(self.frontier) == 0   # to see if the frontier is empty

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node= self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
        

