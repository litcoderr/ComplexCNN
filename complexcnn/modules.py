# -*- coding: utf-8 -*-
import torch
import torch.nn as nn
import numpy as np

class ComplexConv(nn.Module):
    def __init__(self, in_channel, out_channel, kernel_size, stride=1, padding=0, dilation=1, groups=1, bias=True):
        super(ComplexConv,self).__init__()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.padding = padding

        ## Model components
        self.conv_re = nn.Conv2d(in_channel, out_channel, kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias)
        self.conv_im = nn.Conv2d(in_channel, out_channel, kernel_size, stride=stride, padding=padding, dilation=dilation, groups=groups, bias=bias)
        
    def forward(self, x): # shpae of x : [batch,2,channel,axis1,axis2]
        real = self.conv_re(x[:,0]) - self.conv_im(x[:,1])
        imaginary = self.conv_re(x[:,1]) + self.conv_im(x[:,0])
        output = torch.stack((real,imaginary),dim=1)
        return output
        
#%%
if __name__ == "__main__":
    ## Random Tensor for Input
    ## shape : [batchsize,2,channel,axis1_size,axis2_size]
    ## Below dimensions are totally random
    x = torch.randn((10,2,3,100,100))
    
    # 1. Make ComplexConv Object
    ## (in_channel, out_channel, kernel_size) parameter is required
    complexConv = ComplexConv(3,10,(5,5))
    
    # 2. compute
    y = complexConv(x)

