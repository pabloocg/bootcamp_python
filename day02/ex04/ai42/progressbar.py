import time, os

def progressbar(listy):
    for max in listy:
        maxR = max + 1
    toolbar_width = 40
    start = time.time()
    for i in listy:
        yield i
        os.system("clear")
        elapsed = time.time() - start
        if i == 0:
            estimated = maxR * elapsed
        fill = int((i * toolbar_width) / maxR)
        print(f"ETA: {estimated:.2f}s [{round(((i * 100) / maxR)):3}%] [{'=' * fill}>{' ' * (toolbar_width - 1 - fill)}] {i + 1}/{maxR} | elapsed time {elapsed:.2f}s")
