import runway
import numpy as np
import tensorflow as tf
from PIL import Image
from code import default as dt



@runway.setup(options={'checkpoint': runway.file(is_directory=True)})
def setup(opts):
    pass 
    
@runway.command('translate', inputs={'image': runway.image}, outputs={'image': runway.image})
def translate(net,inputs):
    print("Starting")
    output = dt.defaultrun(inputs['image'])
    print("Done")
    return Image.fromarray((output * 255).astype(np.uint8))

if __name__ == '__main__':
    runway.run(port=8889)