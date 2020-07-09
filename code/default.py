import sys
import cv2
import numpy


def defaultrun(images):
    image = cv2.cvtColor(numpy.array(images), cv2.COLOR_RGB2BGR)


    mask = None

    ambient_intensity = 0.45
    light_intensity = 0.85
    light_source_height = 1.0
    gamma_correction = 1.0
    stroke_density_clipping = 1.2
    enabling_multiple_channel_effects = True

    light_color_red = 1.0
    light_color_green = 1.0
    light_color_blue = 1.0


    from code.ProjectPaintingLight2 import run
    


    imageout = run(image, mask, ambient_intensity, light_intensity, light_source_height,
        gamma_correction, stroke_density_clipping, light_color_red, light_color_green,
        light_color_blue, enabling_multiple_channel_effects)

    return imageout

