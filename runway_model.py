import runway
import numpy as np
import tensorflow as tf
from PIL import Image
from code import default as dt

manipulate_command_inputs = {
    'image': runway.image(description='The input image'),
    'ambient_intensity': runway.number(default=0.45, min=0, max=1, step=0.05),
    'light_intensity': runway.number(default=0.85, min=0, max=1, step=0.05),
    'light_source_height': runway.number(default=1, min=0, max=1, step=0.05),
    'gamma_correction': runway.number(default=1, min=0, max=1, step=0.05),
    'stroke_density_clipping':runway.number(default=1.2, min=0, max=2, step=0.05),
    'light_color_red': runway.number(default=1, min=0, max=1, step=0.05),
    'light_color_green': runway.number(default=1, min=0, max=1, step=0.05),
    'light_color_blue': runway.number(default=1, min=0, max=1, step=0.05)
}
    
@runway.command('translate', inputs=manipulate_command_inputs, outputs={'image': runway.image})
def translate(net,inputs):
    output = dt.defaultrun(inputs)
    return Image.fromarray(np.clip(output,0, 255).astype(np.uint8))

if __name__ == '__main__':
    runway.run(port=8889)