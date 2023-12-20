class Variable:
    def __init__(self,data,generation):
        self.data = data
        # 这个值带的梯度
        self.grad = None
        # 就是这个值的计算者，反向传播回去的时候，往回传播s
        self.creator = None
        # 代数
        self.generation = generation
    def set_creator(self,f,generation):
        '''
        这里的f是算子也就是func的functions
        '''
        self.creator = f
        self.generation = generation
    
    def backforward(self,gy):
        return 
        #funcs = [self.creator]
        #while funcs:
            
        

    