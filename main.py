import pyautogui
import keyboard
import time

def get_window():
    windows = pyautogui.getWindowsWithTitle("Victoria")
    
    if windows:
        return windows[0]
    raise AssertionError("Failed to find window with title - Victoria")

def select_rgo():
    window = get_window()
    (top_x, top_y) = window.topleft

    pyautogui.moveTo(top_x + 200, top_y + 325)
    pyautogui.click()

def close_and_open():
    window = get_window()
    (top_x, top_y) = window.topleft

    pyautogui.moveTo(top_x + 300, top_y + 400)
    pyautogui.click()
    pyautogui.click()

def go_to_first_pop():
    window = get_window()
    (top_x, top_y) = window.topleft

    pyautogui.moveTo(top_x + 125, mid_y + 70)

def go_back():
    window = get_window()
    (top_x, top_y) = window.topleft

    pyautogui.moveTo(top_x + 200, top_y + 270)
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
    window = get_window()
    (top_x, top_y) = window.topleft
    (_, mid_y) = window.midleft

    select_rgo()
    close_and_open()

    # add unsplited pops
    pyautogui.press('a', presses=5)

    go_to_first_pop()

    for i in range(5):

        # go next pop
        pyautogui.moveTo(pop_pos_x, pop_pos_y + 60 * i)
        time.sleep(0.1)
        pyautogui.click()

        # press split
        pyautogui.moveTo(top_x + 100, mid_y - 250)
        for i in range(4):
            pyautogui.click()

        go_back()
    
    # go back to rgo
    pyautogui.moveTo(top_x + 200, top_y + 245)
    pyautogui.click()

def add_craftsman(key):
    """
    Change a pop into craftsman
    You should select a RGO or Factory first in order for this script to work
    """
    window = get_window()
    (top_x, top_y) = window.topleft
    (_, mid_y) = window.midleft

    select_rgo()
    close_and_open()

    # add unsplited pops
    pyautogui.press('a', presses=1)

    go_to_first_pop()

    # convert to craftsman
    pyautogui.moveTo(top_x + 350, mid_y - 325)
    pyautogui.click()

    go_back()

def add_clerk(key):
    """
    Change a pop into cleark
    You should select a RGO or Factory first in order for this script to work
    """
    window = get_window()
    (top_x, top_y) = window.topleft
    (_, mid_y) = window.midleft

    select_rgo()
    close_and_open()

    # add unsplited pops
    pyautogui.press('a', presses=1)

    go_to_first_pop()

    # convert to clerk
    pyautogui.moveTo(top_x + 350, mid_y - 375)
    pyautogui.click()

    go_back()

def main():

    # move faster
    pyautogui.PAUSE = 0.05

    # register hotkeys
    keyboard.on_press_key("space", pause)
    keyboard.on_press_key("z", split_pops)
    keyboard.on_press_key("x", add_clerk)
    keyboard.on_press_key("c", add_craftsman)

    keyboard.wait()

if __name__ == "__main__":
    main()
