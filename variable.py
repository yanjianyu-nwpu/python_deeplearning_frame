class Variable:
    def __init__(self,data):
        self.data = data
        # 这个值带的梯度
        self.grad = None
        # 就是这个值的计算者，反向传播回去的时候，往回传播s
        self.creator = None
    def set_creator(self,f):
        '''
        这里的f是算子也就是func的functions
        '''
        self.creator = f

    