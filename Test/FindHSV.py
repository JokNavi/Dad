import colorsys

#input
(r, g, b) = (255, 0, 0)
#normalize
(r, g, b) = (r / 255, g / 255, b / 255)
#convert to hsv
(h, s, v) = colorsys.rgb_to_hsv(r, g, b)
#expand HSV range
(h, s, v) = (int(h * 179), int(s * 255), int(v * 255))
print('HSV : ', h, s, v)