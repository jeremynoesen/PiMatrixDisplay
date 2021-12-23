"""
Simple loading animation to show when the device is processing
"""

import time
import unicornhat as unicorn
import transition
import filter
import threading

loadingthread = None


def __show():
    """
    Show the loading animation
    """
    # Pixels in order of animation
    pixels = [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7),
              (6, 7), (5, 7), (4, 7), (3, 7), (2, 7), (1, 7), (0, 7),
              (0, 6), (0, 5), (0, 4), (0, 3), (0, 2), (0, 1), (0, 0),
              (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)]

    faded_in = False
    t = threading.currentThread()
    while getattr(t, "loop", True):

        # Do pixel animation
        for i in range(len(pixels)):
            unicorn.clear()

            for j in range(8):
                pixel = pixels[(i + j) % len(pixels)]
                filter.set_pixel(pixel[0], pixel[1], 255, 255, 255)
            unicorn.show()

            # Fade in if showing for the first time
            if faded_in is False:
                faded_in = True
                transition.fade(0, 100, 0.2)

            # Wait before next frane
            time.sleep(0.02)


def show():
    """
    Show the loading animation on the Unicorn HAT
    """
    global loadingthread
    clear()
    loadingthread = threading.Thread(target=__show)
    loadingthread.start()


def clear():
    """
    Clear the loading animation off of the Unicorn HAT
    """
    if loadingthread is not None:
        transition.fade(100, 0, 1)
        loadingthread.loop = False
        unicorn.clear()

