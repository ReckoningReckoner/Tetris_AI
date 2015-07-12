import flipper
import debug

##Blue print for all other blocks
# Each block is represented by 0s (unoccupied) and 1s (occupied)
# For example, the T block is represented as: 
# 111
# 010

class Block:
    #obj is the array represention of an object
    #cases is the number of unique rotations
    #name is the name of the block
    def __init__(self):
        self.obj
        self.cases
        self.name
        
    ##rotaes a block @cases number of times and puts it into an array
    def rotations(self):
        return flipper.all(self.obj, self.cases)      
        
    ##returns the type of block
    def type(self):
        return self.name
        
class T_Block(Block):
    def __init__(self):
        self.obj = [[1,1,1],[0,1,0]]
        self.cases = 4
        self.name = "T"
        
class Z_Block(Block):
    def __init__(self):
        self.obj = [[1,1,0],[0,1,1]]
        self.cases = 2
        self.name = "Z"
        
class O_Block(Block):
    def __init__(self):
        self.obj = [[1,1],[1,1]]
        self.cases = 1
        self.name = "O"
        
class S_Block(Block):
    def __init__(self):
        self.obj = [[0,1,1],[1,1,0]]
        self.cases = 1
        self.name = "S"
        
class I_Block(Block):
    def __init__(self):
        self.obj = [[1,1,1,1]]
        self.cases = 2
        self.name = "I"

class J_Block(Block):
    def __init__(self):
        self.obj = [[1,1,1],[0,0,1]]
        self.cases = 4
        self.name = "J"
        
class L_Block(Block):
    def __init__(self):
        self.obj = [[1,1,1],[1,0,0]]
        self.cases = 4
        self.name = "L"

blocks = [ T_Block(), 
           Z_Block(), 
           O_Block(), 
           S_Block(), 
           I_Block(),
           J_Block(),
           L_Block()]

for b in blocks:
    print("This is a",b.type(),"Block")
    for r in b.rotations():
        debug.show(r)
        print("")
    
    
#Output from this program if you wanna check if it's working:
# This is a T Block
# 111
# 010
#
# 01
# 11
# 01
#
# 010
# 111
#
# 10
# 11
# 10
#
# This is a Z Block
# 110
# 011
#
# 01
# 11
# 10
#
# This is a O Block
# 11
# 11
#
# This is a S Block
# 011
# 110
#
# This is a I Block
# 1111
#
# 1
# 1
# 1
# 1
#
# This is a J Block
# 111
# 001
#
# 01
# 01
# 11
#
# 100
# 111
#
# 11
# 10
# 10
#
# This is a L Block
# 111
# 100
#
# 11
# 01
# 01
#
# 001
# 111
#
# 10
# 10
# 11
