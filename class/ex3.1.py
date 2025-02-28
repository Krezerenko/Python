import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    label = tk.Label()
    img = tk.PhotoImage(data=draw(shader, 256, 256)).zoom(2, 2)
    label.pack()
    label.config(image=img)
    tk.mainloop()


def sdf_func(x, y):
    return min(box(x + 0.2, y, 0.05, 0.4), box(x - y + 0.18, y - 0.2, 0.056, 0.21), box(-x - y - 0.18, y + 0.2, 0.056, 0.21))

def box(x, y, w, h):
    dx = abs(x) - w
    dy = abs(y) - h
    return math.hypot(max(dx, 0), max(dy, 0)) + min(max(dx, dy), 0.0)

def shader_1(x, y):
    d = sdf_func(x - 0.5, y - 0.5)
    return d < 0, d < 0, d < 0


main(shader_1)