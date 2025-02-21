import math
import tkinter as tk

root = tk.Tk()
time = 0
label = tk.Label(root)
zoom = 4
windowWidth = 128
windowHeight = 128
windowWidthZ = 256
tickRate = 12
def main():
    img = tk.PhotoImage(data=draw(sh, windowWidth, windowHeight)).zoom(zoom, zoom)
    label.config(image=img)
    label.pack()
    root.bind("<Motion>", on_mouse_move)
    root.bind("<Key>", on_key_pressed)
    root.after(tickRate, update)
    root.mainloop()

def update():
    global time
    time += 5 * tickRate / 1000.0
    # print(time)
    img = tk.PhotoImage(data=draw(sh, windowWidth, windowHeight)).zoom(zoom, zoom)
    label.config(image=img)
    label.image = img
    root.after(tickRate, update)

def on_mouse_move(event):
    global lightSourceX, lightSourceY, lsXScaled, lsYScaled
    lightSourceX = event.x / zoom
    lightSourceY = event.y / zoom
    lsXScaled = lightSourceX / windowWidth
    lsYScaled = lightSourceY / windowHeight

def on_key_pressed(event):
    global lightSourceZ, lsZScaled
    if event.keysym == "Up":
        lightSourceZ += 1
    if event.keysym == "Down":
        lightSourceZ -= 1

    lsZScaled = lightSourceZ / windowWidthZ
    # print(lightSourceZ)

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

ballColor = 0.2, 0.3, 0.4
rad = 40
posX = 64
posY = 64
posZ = 100
radScaled = rad / windowWidth
radSquare = radScaled * radScaled
posXScaled = posX / windowWidth
posYScaled = posY / windowHeight
posZScaled = posZ / windowWidthZ

lsRad = 5
lsRadScaled = lsRad / windowWidth
lightSourceX = 220
lightSourceY = 120
lightSourceZ = -10
lightPower = 0.2
lsXScaled = lightSourceX / windowWidth
lsYScaled = lightSourceY / windowHeight
lsZScaled = lightSourceZ / windowWidthZ

def sh(x, y):
    # Ваш код здесь:
    off_x = x - posXScaled
    off_y = y - posYScaled
    circle_distance = radSquare - off_x**2 - off_y**2
    color = ballColor
    if abs(x - lsXScaled) < lsRadScaled and abs(y - lsYScaled) < lsRadScaled:
        return 1, 1, 1
    if circle_distance < 0:
        return 0, 0, 0
    z = -math.sqrt(circle_distance) + posZScaled

    ls_ball_distance_x = x - posXScaled
    ls_ball_distance_y = y - posYScaled
    ls_ball_distance_z = z - posZScaled
    ls_ball_distance_squared = ls_ball_distance_x**2 + ls_ball_distance_y**2 + ls_ball_distance_z**2 - radSquare
    # if ls_ball_distance_x**2 + ls_ball_distance_y**2 + ls_ball_distance_z**2 < radSquare:
    #     return tuple(c * 0.5 for c in color)

    ls_distance_x = lsXScaled - x
    ls_distance_y = lsYScaled - y
    ls_distance_z = lsZScaled - z

    ls_distance_squared = ls_distance_x**2 + ls_distance_y**2 + ls_distance_z**2
    b = ls_distance_x * ls_ball_distance_x + ls_distance_y * ls_ball_distance_y + ls_distance_z * ls_ball_distance_z

    d = b**2 - ls_ball_distance_squared * ls_distance_squared
    if d < 0:
        return color
    a1 = (b - math.sqrt(d)) / ls_distance_squared
    a2 = 2 * b / ls_distance_squared - a1
    a = (abs(a1) > 0.01) * a1 + (abs(a2) > 0.01) * a2
    is_lit = a > -0.2
    relative_ls_power = is_lit * 1 / ls_distance_squared * lightPower
    time_lit = time * 15 * ls_distance_squared
    multiplier = relative_ls_power + noise(x, y, 7 * time) * (not is_lit) + soft_noise(x, y, int(time_lit), int(time_lit) + 1, fract(time_lit)) * is_lit
    return tuple(multiplier * c for c in color)



def int_base(x):
    if x <= 0.01: return 0
    return math.exp(-1 / x)

q1 = int_base(1)
qq1 = int_base(q1)

def int_unsafe(x):
    return 1/2 + (int_base(q1 - int_base(1 - x)) - int_base(q1 - int_base(x))) / 2 / qq1

def perp(a, b, t):
    return a + (b - a) * int_unsafe(t)

def noise(x, y, seed):
    return fract(math.sin(x * y * 276361) * seed)

def fract(x):
    return x - math.floor(x)

def soft_noise(x, y, seed1, seed2, t):
    return perp(noise(x, y, seed1), noise(x, y, seed2), t)

main()