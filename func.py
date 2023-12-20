import variable
import numpy as np


class Function:
    def __call__(self,*inputs):
        self.inputs = [input.data for input in inputs]
        assert len(self.inputs) > 0

        self.generation = 0
        for input in inputs:
            self.generation = max(self.generation,input.generation)

        ys = self.forward(self.inputs)
        outputs = [variable(ys,self.generation+1) for y in ys] 

        return outputs
    def forward(self,*xs):
        raise NotImplementedError()

class Square(Function):
    def forward(self,x):
        assert len(self.inputs) == 1
        return x ** 2
    def backword(self,dy):
        return 2*self.input.data*dy


def square(x):
    return Square()(x)

class Exp(Function):
    def forward(self,x):
        assert len(self.inputs) == 1
        return np.exp(x.data)
    def backword(self,dy):
        x = self.input.data
        return np.exp(x.data)*dy
def exp(x):
    return exp()(x)

def SquareSun(Function):
    def forward(self,x0,x1):
        assert len(self.inputs) == 2
        return 2*x0*x0+x1*x1
    def backforward(self,dy):
        x0 = self.inputs[0]
        x1 = self.inputs[1]
        return 4*x0+2*x1

def squaresum(x,b):
    return SquareSun()(x,b)


if __name__ == '__main__':
    x = variable.Variable(np.array(10),0)
    a = square(x) 
    y = squaresum(x,a)
    print(y.data)
    