import variable
import numpy as np

class Function:
    def __call__(self,input):
        x = input.data
        self.input = input
        y = self.forward(x)
        output = variable.Variable(y)
        self.output = output
        self.output.set_creator(self)
        return output
    def forward(self,x):
        raise NotImplementedError()

class Square(Function):
    def forward(self,x):
        return x ** 2
    def backword(self,dy):
        return 2*self.input.data*dy

class Exp(Function):
    def forward(self,x):
        return np.exp(x.data)
    def backword(self,dy):
        x = self.input.data
        return np.exp(x.data)*dy

if __name__ == '__main__':
    x = variable.Variable(np.array(10))
    f = Exp()
    print(f(x).data)