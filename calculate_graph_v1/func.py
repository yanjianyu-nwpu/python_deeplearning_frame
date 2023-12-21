import variable
import numpy as np

class Function:    
    def __call__(self,*inputs):         
        self.raw_inputs = inputs                
        self.inputs = [input.data for input in inputs]        
        assert len(self.inputs) > 0

        self.generation = 0        
       
        for input in inputs:            
            self.generation = max(self.generation,input.generation)
        
        ys = self.forward(self.inputs)                
        outputs = [variable.Variable(y,self.generation+1) for y in ys]         
        self.outputs = outputs        
        
        for o in outputs:            
            o.creator = self                    
            
            return outputs   
    def forward(self,*xs):        
        raise NotImplementedError()
        
    def backforward(self):        
        raise NotImplementedError()

class Square(Function):    
    def forward(self,x):        
        assert len(self.inputs) == 1        
        return [x[0] ** 2]    
    
    def backforward(self,dy):      
        assert len(dy) == 1        
        dy = dy[0]        
        return [2*self.inputs[0]*dy]

def square(x):    
    return Square()(x)[0]

class Exp(Function):    
    def forward(self,x):        
        assert len(self.inputs) == 1        
        return [np.exp(x[0].data)]    
    
    def backforward(self,dy):        
        assert len(dy) == 1        
        g = dy[0]        
        x = self.input.data        
        return dy[0]*[np.exp(x[0].data)*g]
    
    def exp(x):    
        return exp()(x)[0]
    
class SquareSun(Function):    
    def forward(self,x):        
        assert len(self.inputs) == 2        
        return [2*x[0]*x[0]+x[1]*x[1]]    
    
    def backforward(self,dy):        
        assert len(dy) == 1                
        g = dy[0]        
        x0 = self.inputs[0]        
        x1 = self.inputs[1]        
        return [4*x0*g,2*x1*g]
    
def squaresum(x,b):    
    l = SquareSun()(x,b)    
    return l[0]

if __name__ == '__main__':    
    x = variable.Variable(np.array(10),0)    
    a = square(x)     
    y = squaresum(x,a)        
    y.grad = 1.0    
    y.backforward()        
    print(a.grad)    
    print(x.grad)