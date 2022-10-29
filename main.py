import pyautogui
import keyboard

def move_to(x, y):
    window = get_window()
    (top_x, top_y) = window.topleft

    is_windowed_mode = window.size.width != 1024 and window.size.height != 768
    screen_title_offset = 31 if is_windowed_mode else 0

    pyautogui.moveTo(top_x + x, top_y + y + screen_title_offset)

def add_pops(n):
    # add pops into rgo
    # trick: pops will be added according to their size (bigger pops will be added first)
    pyautogui.press('a', presses=n)

def get_window():
    windows = pyautogui.getWindowsWithTitle("Victoria")
    
    if windows:
        return windows[0]
    raise AssertionError("Failed to find window with title - Victoria")

def select_rgo():
    rgo_box_pos = (35, 146)
    move_to(*rgo_box_pos)
    pyautogui.click()

def close_and_open():
    open_rgo_btn_pos = (155, 174)

    # closing and then reopening rgo will empty it
    move_to(*open_rgo_btn_pos)
    pyautogui.click()
    pyautogui.click()

def go_back():
    go_to_rgo_btn_pos = (125, 110)
    move_to(*go_to_rgo_btn_pos)
    pyautogui.click()

def get_first_pop_pos():
    return (125, 399)

def select_first_pop():
    move_to(*get_first_pop_pos())
    pyautogui.click()

def pause(key):
    """
    send pause event
    """
    pyautogui.press("pause")

def split_pops(key):
    """
    split pops for both RGOs and Factories
    You should select a RGO or Factory first in order for this script to work
    """
    max_visible_pops = 5
    split_pop_btn_pos = (52, 245)

    select_rgo()
    close_and_open()

    add_pops(n=max_visible_pops)
    pyautogui.sleep(0.08)

    for i in range(max_visible_pops):
        pop_offset = 40
        first_pop_pos = get_first_pop_pos()
    
        move_to(first_pop_pos[0], first_pop_pos[1] + (i * pop_offset))
        pyautogui.click()

        move_to(*split_pop_btn_pos)
        for _ in range(5):
            pyautogui.click()

        go_back()

def _add_new(pop_class):
    select_rgo()
    close_and_open()
    add_pops(n=1)
    select_first_pop()
    if pop_class == "craftsman":
        move_to(153, 210)
        pyautogui.click()
    elif pop_class == "clerk":
        move_to(153, 190)
        pyautogui.click()
    go_back()
        
def add_craftsman(key):
    """
    Change a pop into craftsman
    You should select a RGO or Factory first in order for this script to work
    """
    _add_new(pop_class="craftsman")

def add_clerk(key):
    """
    Change a pop into cleark
    You should select a RGO or Factory first in order for this script to work
    """
    _add_new(pop_class="clerk")

def main():
    print('pyvickeys is running\n')
    print('** help **')
    print('space - pause')
    print('z - split pops')
    print('x - add clerks')
    print('c - add craftsman')
    print('q - exit program')

    # move faster
    pyautogui.PAUSE = 0.03

    # register hotkeys
    keyboard.on_press_key("space", pause)
    keyboard.on_press_key("z", split_pops)
    keyboard.on_press_key("x", add_clerk)
    keyboard.on_press_key("c", add_craftsman)

    # exits when hotkey is pressed
    keyboard.wait(hotkey="q")

if __name__ == "__main__":
    main()
