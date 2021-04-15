from torch import nn
from torch.nn.modules.utils import _pair

import functional as F


class Aggregation(nn.Module):

    def __init__(self, kernel_size, stride, padding, dilation, pad_mode):
        super(Aggregation, self).__init__()
        self.kernel_size = _pair(kernel_size)
        self.stride = _pair(stride)
        self.padding = _pair(padding)
        self.dilation = _pair(dilation)
        self.pad_mode = pad_mode

    def forward(self, input, weight):
        # print(self.kernel_size)
        # print(self.stride)
        # print(self.padding)
        # print(self.dilation)
        return F.aggregation(input, weight, self.kernel_size, self.stride, self.padding, self.dilation, self.pad_mode)