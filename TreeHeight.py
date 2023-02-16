# https://app.codility.com/programmers/trainings/4/tree_height/
from extratypes import Tree  # library with types used in the task
from queue import Queue

def solution(T):
    height = 0
    queue = Queue()
    queue.put((T,0))

    while not queue.empty():
        current_node = queue.get()
        height =  current_node[1]

        if current_node[0].l:
            queue.put((current_node[0].l, height+1))

        if current_node[0].r:
            queue.put((current_node[0].r, height+1))
    return height
