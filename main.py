import tkinter as tk


def collatz_this(old_number):
    if (int(old_number)):
        if old_number % 2 == 0:
            new_number = old_number / 2
        else:
            new_number = (old_number * 3) + 1
        return int(new_number)
    else:
        print("NaN dummy!")
        return None


def bg_color_change():
    global start_num
    start_num += 1
    old_current_num, current_num = collatz_main(start_num)
    # these numbers need some kind of adjustment to make colors more interesting and less //red monotone
    red_rgb = hex(start_num % 255)[2:]
    blue_rgb = hex(((old_current_num % 255) * 100) % 255)[2:]
    green_rgb = hex(((current_num % 255) * 100) % 255)[2:]
    window.configure(bg="#"
                        + red_rgb.zfill(2)
                        + blue_rgb.zfill(2)
                        + green_rgb.zfill(2))
    # first number is how often window updates
    window.after(10, bg_color_change)


def collatz_main(start_num):
    current_num = start_num
    old_current_num = current_num
    while current_num > 1:
        old_current_num = current_num
        current_num = collatz_this(current_num)
        print(str(old_current_num) + " becomes " + str(current_num))
    return old_current_num, current_num


start_num = 3
window = tk.Tk()
window.geometry("200x200")
bg_color_change()
window.mainloop()
