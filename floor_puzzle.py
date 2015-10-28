import itertools

def is_on_higher_floor(f1, f2):
    "floor f1 is higher than floor f2"
    return f1>f2

def is_adjacent_to(f1, f2):
    "Two floors are adjacent to each other if they differ by 1."
    return abs(f1-f2) == 1

def my_floor_puzzle():
    "Return a tuple (hopper,kay,liskov,perlis,ritchie) numbers."
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors)) # 1
    return list(next((hopper, kay, liskov, perlis, ritchie)
                for (hopper, kay, liskov, perlis, ritchie) in orderings
                if not hopper is top
                if not kay is bottom
                if not liskov is top and not liskov is bottom
                if is_on_higher_floor(perlis,kay)
                if not is_adjacent_to(ritchie, liskov)
                if not is_adjacent_to(liskov, kay)
                ))

def floor_puzzle():
    "Return a tuple (hopper,kay,liskov,perlis,ritchie) numbers."
    floors = bottom, _, _, _, top = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(floors))
    for (hopper, kay, liskov, perlis, ritchie) in orderings:
        if (hopper is not top
            and kay is not bottom
            and liskov is not top
            and liskov is not bottom
            and perlis > kay
            and abs(ritchie - liskov) > 1
            and abs(liskov - kay) >1):
            return [hopper, kay, liskov, perlis, ritchie]            

import time

def timedcall(fn, *args):
    "Call function with args; return the time in seconds and result."
    t0 = time.clock()
    result = fn(*args)
    t1 = time.clock()
    return t1-t0, result

def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers)) 

def my_timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    # Your code here.
    if isinstance(n, int):
        times = [timedcall(fn,*args)[0] for _ in range(n)]
    else:
        times = []
        elapsed_total = 0
        while (elapsed_total < n):
            (elapsed_time,result) = timedcall(fn,*args)
            elapsed_total+=elapsed_time
            times.append(elapsed_time)
    return min(times), average(times), max(times)

def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timedcall(fn,*args)[0] for _ in range(n)]
    else:
        times = []
        while (sum(times) < n):
            times.append(timedcall(fn,*args)[0]) # arg0 is the time
    return min(times), average(times), max(times)


print floor_puzzle()
