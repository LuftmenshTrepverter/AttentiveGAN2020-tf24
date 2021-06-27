"""

"""
from easydict import EasyDict as edict

__C = edict()

cgf = __C

__C.TRAIN = edict()

__C.TRAIN.EPOCHS = 100010
# Set the initial learning rate
__C.TRAIN.LEARNING_RATE = 0.002
# Set the GPU resource used during training process
__C.TRAIN.GPU_MEMORY_FRACTION = 0.9
# Set the GPU allow growth parameter during tensorflow training process
__C.TRAIN.TF_ALLOW_GROWTH = True
# Set the shadownet training batch size
__C.TRAIN.BATCH_SIZE = 1
# Set train image height
#__C.TRAIN.IMG_HEIGHT = 256
__C.TRAIN.IMG_HEIGHT = 256
# Set train image width
#__C.TRAIN.IMG_WIDTH = 376
__C.TRAIN.IMG_WIDTH = 376
# Set train image height
#__C.TRAIN.CROP_IMG_HEIGHT = 240
__C.TRAIN.CROP_IMG_HEIGHT = 240
# Set train image width
#__C.TRAIN.CROP_IMG_WIDTH = 360
__C.TRAIN.CROP_IMG_WIDTH = 360
# Set cpu multi process thread nums
__C.TRAIN.CPU_MULTI_PROCESS_NUMS = 32
# Set the GPU nums
__C.TRAIN.GPU_NUM = 1

# Test options
__C.TEST = edict()

# Set the GPU resource used during testing process
__C.TEST.GPU_MEMORY_FRACTION = 0.8
# Set the GPU allow growth parameter during tensorflow testing process
__C.TEST.TF_ALLOW_GROWTH = False
# Set the test batch size
__C.TEST.BATCH_SIZE = 1
# Set test image height
__C.TEST.IMG_HEIGHT = 480
# Set test image width
__C.TEST.IMG_WIDTH = 180
