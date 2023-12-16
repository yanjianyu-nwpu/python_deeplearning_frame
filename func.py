import variable
import numpy as np

class Function:
    def __call__(self,input):
        x = input.data
        y = self.forward(x)
        output = variable.Variable(y)
        return output
    def forward(self,x):
        raise NotImplementedError()

class Square(Function):
    def forward(self,x):
        return x ** 2

class Exp(Function):
    def forward(self,x):
        return np.exp(x.data)

if __name__ == '__main__':
    x = variable.Variable(np.array(10))
    f = Exp()
    print(f(x).data)