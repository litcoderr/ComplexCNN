# ComplexCNN
pytorch implementation of complex convolutional neural network
Reference: [https://arxiv.org/pdf/1705.09792.pdf](https://arxiv.org/pdf/1705.09792.pdf)

## For whom?
When using complex numbers as a domain of a neural network (such as speech enhancement) deep complex networks can be very effective. <br>
[Phase-Aware Speech Enhancement with Deep Complex U-Net](https://openreview.net/forum?id=SkeRTsAcYm) is a great example. Use this as a building block of complex number targeted architecture.

## Usage
### 0. Install Package
```
pip install complexcnn
```

### 1. Preprocess Input
```python
# Suppose X is a complex vector shape of [batch,channel,axis1,axis2]
X = np.stack((X.real,X.imag),axis=1) # shape: [batch,2,channel,axis1,axis2]
```

### 2. ComplexConv Module
#### Parameters
Same as Pytorch Conv2d Parameters

- in_channel (required)
- out_channel (required)
- kernel_size (required)
- stride (default: 1)
- padding (default: 0)
- dilation (default: 1)
- groups (default: 1)
- bias (default: True)

#### Input

- Tensor (Type: torch.Tensor) shape: (batchsize, 2, input channel, axis1, axis2)

#### Output

- Tensor (Type: torch.Tensor) shape: (batchsize, 2, output channel, axis1, axis2)

```python
from complexcnn.modules import ComplexConv

## Parameters Below are totally random
input_channel = 3
output_channel = 24
kernel_size = (5,5)

complex_conv = ComplexConv(input_channel, output_channel, kernel_size)

Y = complex_conv(X)
```