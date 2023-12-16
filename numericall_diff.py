from variable import *

def numerical_diffs(f,x,eps=1e-4):
    '''
    实现数值微分，就是求斜率
    '''
    x0 = Variable(x.data-eps)
    x1 = Variable(x.data+eps)

    y0 = f(x0)
    y1 = f(x1)

    return (y1.data-y0.data)/(2*eps)