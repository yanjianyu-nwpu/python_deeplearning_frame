def generation(elem):    
        return elem.generation
class Variable:    
    def __init__(self,data,generation):        
        self.data = data        
        # 这个值带的梯度        
        self.grad = 0.0        
        # 就是这个值的计算者，反向传播回去的时候，往回传播s        
        self.creator = None        # 代数        
        self.generation = generation    
        
    def set_creator(self,f,generation):        
        '''        
        这里的f是算子也就是func的functions        
        '''        
        
        self.creator = f        
        self.generation = generation        
    def backforward(self):        
        funcs = [self.creator]          
        while funcs:            
            f = funcs.pop()
        
            preGrads = [v.grad for v in f.outputs]                
            gradList = f.backforward(preGrads)            
            for v,grad in zip(f.raw_inputs,gradList):                
                v.grad = v.grad + grad                        
            for v in f.raw_inputs:                
                if v.creator == None:                    
                    continue                
                funcs.append(v.creator)            
            funcs.sort(key= generation)                         
        return      