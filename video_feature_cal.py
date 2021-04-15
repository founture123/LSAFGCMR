import torch.nn.functional as F
from retrieval import *
post = [25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 7, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 23, 25, 23, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 19, 25, 24, 22, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 24, 25, 22, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 21, 25, 24, 24, 25, 25, 24, 23, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 24, 18, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 24, 25, 19, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 18, 25, 25, 24, 25, 25, 22, 21, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 24, 25, 25, 24, 25, 25, 25, 24, 25, 25, 23, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 20, 25, 25, 25, 25, 25, 24, 22, 25, 25, 21, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 24, 12, 25, 25, 25, 25, 24, 16, 24, 24, 25, 8, 25, 24, 25, 25, 24, 25, 22, 25, 25, 17, 12, 25, 25, 25, 25, 25, 25, 25, 19, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 24, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 19, 25, 25, 25, 24, 25, 24, 25, 25, 24, 25, 23, 24, 25, 25, 25, 25, 25, 25, 24, 24, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 22, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 24, 25, 24, 25, 25, 21, 25, 25, 25, 23, 25, 25, 25, 18, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 18, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 16, 25, 25, 25, 25, 23, 24, 25, 24, 24, 25, 25, 25, 25, 25, 24, 22, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 24, 25, 22, 25, 25, 24, 25, 20, 25, 25, 20, 24, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 18, 25, 19, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 21, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 23, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 22, 25, 25, 25, 6, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 22, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 24, 25, 25, 20, 25, 25, 25, 25, 24, 25, 25, 25, 24, 20, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 24, 24, 25, 23, 25, 25, 25, 22, 25, 25, 25, 24, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 23, 24, 16, 24, 14, 25, 25, 25, 25, 17, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 22, 25, 24, 25, 21, 25, 25, 25, 25, 25, 23, 25, 10, 25, 25, 24, 15, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 17, 25, 25, 25, 25, 25, 24, 25, 25, 1, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 23, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 17, 22, 25, 25, 25, 25, 24, 25, 24, 24, 23, 25, 25, 7, 25, 25, 25, 14, 25, 25, 25, 25, 25, 23, 24, 24, 25, 24, 25, 25, 21, 25, 25, 25, 25, 15, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 21, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 20, 22, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 3, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 24, 24, 11, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 24, 23, 23, 25, 25, 25, 25, 24, 25, 24, 25, 25, 24, 15, 24, 25, 25, 25, 24, 25, 25, 25, 24, 24, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 14, 25, 25, 25, 25, 25, 25, 16, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 23, 23, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 24, 24, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 21, 24, 25, 25, 25, 24, 25, 24, 25, 25, 22, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 24, 24, 24, 25, 25, 25, 25, 23, 25, 19, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 23, 25, 25, 25, 25, 25, 25, 25, 22, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 3, 23, 24, 25, 24, 25, 25, 23, 25, 25, 24, 21, 25, 25, 25, 22, 25, 25, 25, 25, 24, 25, 25, 23, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 24, 24, 20, 25, 25, 25, 25, 25, 24, 25, 25, 25, 21, 24, 25, 24, 25, 25, 23, 25, 25, 18, 24, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 23, 22, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 16, 25, 25, 24, 25, 25, 24, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 24, 25, 20, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 22, 25, 25, 25, 24, 23, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 24, 23, 24, 25, 24, 25, 23, 24, 24, 25, 25, 25, 24, 25, 24, 17, 25, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 24, 25, 25, 25, 25, 25, 23, 25, 25, 25, 12, 22, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 19, 25, 24, 23, 24, 18, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 20, 17, 25, 25, 25, 25, 23, 25, 23, 25, 25, 24, 25, 25, 25, 24, 23, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 24, 25, 25, 25, 21, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 24, 25, 25, 25, 24, 22, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 24, 25, 22, 24, 24, 25, 23, 25, 25, 25, 24, 25, 25, 22, 25, 25, 19, 25, 25, 25, 25, 23, 24, 24, 25, 25, 24, 24, 25, 25, 25, 19, 23, 25, 18, 24, 25, 25, 25, 25, 25, 20, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 24, 23, 25, 25, 16, 24, 25, 25, 25, 25, 25, 11, 5, 25, 23, 25, 5, 25, 25, 25, 25, 24, 21, 24, 25, 12, 25, 25, 25, 23, 8, 25, 25, 25, 24, 24, 12, 25, 25, 25, 25, 4, 19, 25, 16, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 20, 25, 24, 25, 25, 25, 25, 25, 25, 24, 24, 25, 24, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 21, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 17, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 17, 25, 21, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 22, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 17, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 25, 25, 20, 25, 25, 25, 25, 24, 24, 25, 24, 25, 25, 23, 25, 25, 25, 25, 21, 21, 25, 24, 25, 25, 24, 25, 25, 25, 21, 25, 25, 25, 25, 24, 25, 24, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 24, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 23, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 19, 25, 25, 25, 24, 25, 24, 25, 25, 25, 23, 19, 25, 25, 25, 25, 25, 25, 24, 21, 25, 25, 24, 25, 25, 25, 24, 22, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 20, 25, 25, 25, 25, 25, 25, 24, 24, 25, 24, 22, 25, 25, 25, 25, 25, 25, 25, 25, 21, 23, 18, 25, 25, 25, 17, 24, 24, 25, 25, 1, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 23, 25, 25, 25, 24, 23, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 21, 25, 24, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 18, 24, 25, 25, 25, 25, 25, 25, 25, 25, 20, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 16, 25, 25, 24, 25, 25, 25, 25, 21, 25, 24, 25, 17, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 21, 25, 25, 25, 25, 25, 2, 25, 24, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 2, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 22, 24, 24, 23, 22, 25, 25, 25, 25, 25, 21, 25, 23, 24, 25, 24, 25, 25, 23, 25, 23, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 23, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 11, 25, 24, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 24, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 24, 25, 18, 25, 25, 25, 25, 23, 25, 25, 25, 23, 25, 24, 24, 24, 25, 24, 25, 23, 25, 25, 25, 25, 21, 25, 25, 25, 18, 25, 25, 25, 25, 24, 25, 24, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 15, 25, 25, 25, 25, 25, 25, 25, 25, 25, 21, 24, 25, 24, 24, 24, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 21, 25, 24, 25, 3, 25, 25, 25, 24, 25, 25, 25, 23, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 23, 24, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 7, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 19, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 23, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 8, 25, 25, 25, 25, 24, 14, 24, 25, 25, 25, 25, 24, 25, 24, 24, 19, 25, 25, 25, 25, 25, 18, 25, 24, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 24, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 22, 24, 24, 25, 24, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 20, 25, 24, 25, 25, 24, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 2, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 14, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 6, 25, 25, 25, 25, 25, 25, 19, 25, 25, 24, 23, 25, 25, 25, 25, 25, 25, 11, 22, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 20, 25, 25, 25, 21, 25, 24, 25, 25, 24, 25, 25, 21, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 24, 25, 25, 21, 25, 25, 24, 25, 25, 25, 25, 6, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 24, 21, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 2, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 21, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 19, 25, 25, 24, 25, 25, 25, 24, 25, 24, 25, 25, 24, 25, 25, 25, 24, 24, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 11, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 24, 24, 19, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 20, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 18, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 24, 25, 25, 25, 25, 24, 22, 24, 25, 23, 25, 24, 25, 25, 25, 25, 24, 8, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 1, 24, 25, 25, 24, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 14, 25, 25, 24, 25, 25, 25, 25, 24, 23, 25, 24, 25, 25, 25, 24, 21, 24, 23, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 24, 25, 17, 25, 24, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 23, 24, 25, 25, 25, 25, 25, 25, 4, 25, 25, 25, 23, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 24, 22, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 21, 25, 25, 24, 24, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 23, 20, 25, 25, 25, 16, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 20, 25, 24, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 19, 25, 25, 24, 25, 25, 21, 23, 25, 23, 20, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 24, 24, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 18, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 24, 24, 24, 25, 25, 25, 25, 24, 25, 24, 23, 25, 24, 25, 4, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 22, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 22, 21, 25, 16, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 19, 11, 23, 25, 11, 24, 25, 25, 25, 25, 24, 25, 25, 24, 7, 25, 25, 25, 24, 25, 25, 25, 11, 24, 25, 25, 25, 14, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 21, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 24, 25, 25, 25, 25, 25, 25, 25, 23, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 24, 24, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 22, 24, 13, 25, 25, 22, 24, 24, 25, 25, 25, 25, 25, 25, 24, 25, 21, 25, 25, 25, 25, 25, 24, 25, 25, 25, 22, 23, 25, 23, 25, 25, 25, 25, 25, 25, 23, 24, 25, 24, 25, 24, 24, 25, 25, 22, 25, 25, 23, 23, 24, 24, 25, 22, 24, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 23, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 24, 24, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 18, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 10, 25, 20, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 11, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 21, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 24, 1, 25, 25, 25, 25, 25, 25, 25, 25, 25, 21, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 9, 25, 25, 25, 24, 25, 25, 22, 23, 25, 25, 24, 25, 24, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 24, 25, 25, 24, 25, 25, 18, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 8, 25, 25, 25, 24, 25, 19, 25, 17, 25, 25, 25, 25, 25, 24, 25, 25, 25, 3, 25, 23, 25, 25, 25, 25, 25, 25, 21, 25, 25, 25, 25, 25, 25, 25, 16, 22, 24, 25, 24, 25, 24, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 9, 25, 25, 22, 25, 25, 19, 25, 24, 25, 24, 22, 25, 25, 25, 25, 24, 25, 25, 24, 24, 25, 25, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 24, 25, 25, 23, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 22, 25, 25, 24, 24, 23, 25, 25, 25, 25, 25, 25, 23, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 5, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 16, 25, 24, 24, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 5, 25, 25, 25, 25, 25, 25, 25, 25, 2, 24, 19, 24, 25, 25, 25, 25, 25, 25, 23, 23, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 20, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 18, 21, 10, 25, 24, 22, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 24, 25, 25, 25, 25, 1, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 24, 24, 25, 25, 25, 25, 12, 25, 25, 24, 24, 24, 25, 24, 25, 25, 21, 25, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 23, 25, 24, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 24, 24, 25, 25, 24, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 24, 25, 25, 21, 24, 25, 25, 24, 1, 24, 24, 25, 24, 25, 24, 24, 25, 24, 24, 24, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 23, 25, 25, 25, 24, 25, 25, 25, 25, 25, 22, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 24, 25, 25, 25, 14, 25, 25, 25, 25, 25, 25, 24, 25, 25, 24, 21, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 23, 24, 25, 24, 25, 25, 22, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 22, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 22, 25, 24, 25, 25, 25, 24, 25, 23, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 23, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 17, 25, 23, 25, 25, 25, 25, 25, 25, 25, 25, 22, 17, 25, 25, 25, 25, 25, 25, 25, 25, 23, 25, 25, 25, 25, 25, 24, 25, 25, 16, 25, 25, 25, 24, 25, 24, 25, 25, 25, 23, 25, 25, 21, 25, 24, 24, 24, 25, 25, 25, 25, 25, 19, 25, 24, 23, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 24, 24, 25, 24, 23, 25, 24, 24, 9, 25, 25, 25, 24, 25, 25, 25, 24, 25, 25, 24, 25, 24, 25, 25, 25, 23, 22, 25, 23, 24, 25, 25, 25, 25, 25, 25, 22, 25, 25, 25, 25, 25, 24, 24, 25, 25, 24, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 25, 25, 25, 25, 23, 25, 25, 25, 24, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 24, 25, 24, 25, 20, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 25, 24, 20, 24, 25, 25, 25, 25, 25, 25, 24, 24, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 19, 25, 25, 25, 25, 25, 25, 25, 25, 25, 24, 25, 25, 25, 25, 25, 25, 25, 24, 25, 24, 24, 25, 25, 24, 24, 25, 25, 25, 24, 25, 21, 25, 25, 25, 25, 24, 24]
os.environ["CUDA_VISIBLE_DEVICES"] = "3"
def mean():
    pop = []
    outs = np.loadtxt("vector_video_feature/san_out_video/features_te.txt", dtype=np.float64)
    print(outs.shape)
    m = 0
    i = 0
    flage = True
    sum = 0
    num = 0
    for k in post:
        sum += k
    f = np.zeros((sum, 200))
    for out in outs:
        out = torch.Tensor(out).cuda().reshape(1,200)

        i += 1
        if i == post[m]:
            i = 0
            m += 1
            outs = torch.cat((out, outs), 0)
            # print("outs",outs.size())
            output = torch.mean(outs, 0).reshape(1, 200)
            output = F.softmax(output, dim=1).detach().cpu().numpy()
            # print(output)
            num += output.shape[0]
            # print(m)
            if ((m - 1) == len(post) - 1):
                f[(m - 1) :num, :] = output
            else:
                f[(m - 1) :(m) , :] = output

            flage = True


        else:
            if flage:
                outs = out
                flage = False
            else:
                outs = torch.cat((out,outs),0)

    np.savetxt('vector_video_feature/san_calout_video/features_te.txt', f[:num, :])




if __name__ == '__main__':
    mean()