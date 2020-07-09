import runway
import numpy as np
import tensorflow as tf
from PIL import Image
from code import default as dt


# ambient_intensity = 0.45
# light_intensity = 0.85
# light_source_height = 1.0
# gamma_correction = 1.0
# stroke_density_clipping = 1.2
# light_color_red = 1.0
# light_color_green = 1.0
# light_color_blue = 1.0

# features = 'ambient_intensity light_intensity light_source_height gamma_correction stroke_density_clipping light_color_red light_color_green light_color_blue'
# features = features.split()

# manipulate_command_inputs = {
#   'image': runway.image(description='The input image containing a face to transform.'),
#   'feature': runway.category(choices=features, default=features[2]),
#   'amount': runway.number(default=0.5, min=0, max=1, step=0.1)
# }

@runway.setup(options={'checkpoint': runway.file(is_directory=True)})
def setup(opts):
    pass 
    
@runway.command('translate', inputs={'image': runway.image}, outputs={'image': runway.image})
def translate(net,inputs):
    print("Starting")
    output = dt.defaultrun(inputs['image'])
    print("Done")
    return Image.fromarray(np.clip(output,0, 255).astype(np.uint8))

if __name__ == '__main__':
    runway.run(port=8889)