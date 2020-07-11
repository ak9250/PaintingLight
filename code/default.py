import sys
import cv2
import numpy


def defaultrun(inputs):
    images = inputs['image']
    image = numpy.array(images)
    image = image[..., ::-1]

    mask = None
    ambient_intensity = inputs['ambient_intensity']
    light_intensity = inputs['light_intensity']
    light_source_height = inputs['light_source_height']
    gamma_correction = inputs['gamma_correction']
    stroke_density_clipping = inputs['stroke_density_clipping']
    enabling_multiple_channel_effects = True

    light_color_red = inputs['light_color_red']
    light_color_green = inputs['light_color_green']
    light_color_blue = inputs['light_color_blue']


    from code.ProjectPaintingLight2 import run
    


    imageout = run(image, mask, ambient_intensity, light_intensity, light_source_height,
        gamma_correction, stroke_density_clipping, light_color_red, light_color_green,
        light_color_blue, enabling_multiple_channel_effects)
    
    imageout = imageout[..., ::-1]
    
    return imageout

