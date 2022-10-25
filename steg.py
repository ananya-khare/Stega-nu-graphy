def hide(rgb_image,binary_data):
    size = rgb_image.size
    to_hide = iter("".join(binary_data)+"0000000")
    pixels = rgb_image.load()
    for x in range(size[0]):
        for y in range(size[1]):
            r,g,b = pixels[x,y]
            try:
                temp = next(to_hide)
                r = list(format(r,'#010b')[2:])
                r[-1] = temp
                r = int("".join(r),2)
                temp = next(to_hide)
                g = list(format(g,'#010b')[2:])
                g[-1] = temp
                g = int("".join(g),2)
                temp = next(to_hide)
                b = list(format(b,'#010b')[2:])
                b[-1] = temp
                b = int("".join(b),2)
            except:
                pixels[x,y] = (r,g,b)
                break
            pixels[x,y] = (r,g,b)       
    return rgb_image