from numpy import block
import pygame
from consts import *
import numpy as np
import random
import time
    
pygame.init()
pygame.display.set_caption("Algorithm Visualizer")
WIDTH, HEIGHT = 1300, 525
block_size = 25
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
clock = pygame.time.Clock()
font = pygame.font.Font(None, 16)
arr = list(range(1,51))
arr = [random.randint(-99,99) for _ in range(50)]
delay = 50
print(arr)

def draw():
    screen.fill(BACKGROUD_COLOUR)
    index = 0
    for x in range(0, screen.get_width(), block_size):
        for y in range(0, screen.get_height(), block_size):
            if y == (screen.get_height() - block_size)//2 and x >= block_size and x<= len(arr)*block_size:
                rect = pygame.Rect(x, y, block_size, block_size)
                text_rect = pygame.Rect((x+block_size//4), (y+block_size//4), block_size, block_size)
                pygame.draw.rect(screen, BLACK, rect, 0)
                text = font.render(f"{arr[index]}", True, BACKGROUD_COLOUR)
                text_rect = text.get_rect()
                text_rect.center = rect.center
                screen.blit(text, text_rect)
                index += 1
            else:
                pygame.draw.rect(screen, BLACK, pygame.Rect(x, y, block_size, block_size), 1)
    pygame.display.update()

def draw_selection_sort(arr, order_array_len=len(arr), i=-1, j=-1):
    screen.fill(BACKGROUD_COLOUR)
    index = 0
    for x in range(block_size, block_size*(len(arr)+1), block_size):
        y = screen.get_height() // 2 - 1*block_size
        rect = pygame.Rect(x, y, block_size, block_size)
        text_rect = rect
        if index < order_array_len:
            pygame.draw.rect(screen, GREEN, rect, 0)
        if index == i:
            pygame.draw.rect(screen, RED, rect, 0)
        if index == j:
            pygame.draw.rect(screen, BLUE, rect, 0)
        pygame.draw.rect(screen, BLACK, rect, 1)
        text = font.render(f"{arr[index]}", True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = rect.center
        screen.blit(text, text_rect)
        index += 1
    pygame.display.update()

def draw_merge_sort(arr, start=0, end=len(arr)-1, mid=-1, i=-1, j=-1, k=-1, arr_=[], left=[], right=[], all_green=False):
    screen.fill(BACKGROUD_COLOUR)
    index = 0
    y = screen.get_height() // 2 - 1*block_size
    for x in range(block_size, block_size*(len(arr)+1), block_size):
        rect = pygame.Rect(x, y, block_size, block_size)
        text_rect = rect
        if not all_green:
            if index > end:
                pygame.draw.rect(screen, GREY, rect, 0)
            if index < start:
                pygame.draw.rect(screen, GREY, rect, 0)
        else:
            pygame.draw.rect(screen, GREEN, rect, 0)
        pygame.draw.rect(screen, BLACK, rect, 1)

        if (index < k  or index > end) or all_green:
            pygame.draw.rect(screen, BLACK, rect, 1)
            text = font.render(f"{arr[index]}", True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = rect.center
            screen.blit(text, text_rect)
        index += 1


    index = 0
    for x in range(block_size, block_size*(len(arr_)+1), block_size):
        rect_below = pygame.Rect(x, y + 2*block_size, block_size, block_size)
        text_rect = rect_below 
        pygame.draw.rect(screen, BLACK, rect_below, 1)
        text = font.render(f"{arr_[index]}", True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = rect_below.center
        screen.blit(text, text_rect)
        index += 1

    index = 0
    for x in range(block_size, block_size*(len(left)+1), block_size):
        rect_below = pygame.Rect(x, y + 4*block_size, block_size, block_size)
        text_rect = rect_below 
        if index == i:
            pygame.draw.rect(screen, RED, rect_below, 0)

        pygame.draw.rect(screen, BLACK, rect_below, 1)
        text = font.render(f"{left[index]}", True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = rect_below.center
        screen.blit(text, text_rect)
        index += 1

    index = 0
    for x in range(block_size, block_size*(len(right)+1), block_size):
        rect_below = pygame.Rect(x, y + 6*block_size, block_size, block_size)
        text_rect = rect_below 
        if index == j:
            pygame.draw.rect(screen, BLUE, rect_below, 0)
        pygame.draw.rect(screen, BLACK, rect_below, 1)
        text = font.render(f"{right[index]}", True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = rect_below.center
        screen.blit(text, text_rect)
        index += 1

    pygame.display.update()


def draw_quick_sort(arr, start=-1, end=-1, pi=-1, all_green=False):
    screen.fill(BACKGROUD_COLOUR)
    index = 0
    for x in range(block_size, block_size*(len(arr)+1), block_size):
        y = screen.get_height() // 2 - 1*block_size
        rect = pygame.Rect(x, y, block_size, block_size)
        text_rect = rect
        if not all_green:
            if index == start:
                pygame.draw.rect(screen, RED, rect, 0)
            if index == end:
                pygame.draw.rect(screen, BLUE, rect, 0)
            if index == pi:
                pygame.draw.rect(screen, GREEN, rect, 0)
        else:
            pygame.draw.rect(screen, GREEN, rect, 0)
        pygame.draw.rect(screen, BLACK, rect, 1)
        text = font.render(f"{arr[index]}", True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = rect.center
        screen.blit(text, text_rect)
        index += 1
    pygame.display.update()


def selection_sort(arr):
    ordered_array_len = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] <= arr[min_index]:
                min_index = j
            draw_selection_sort(arr, ordered_array_len,i, j)
            pygame.time.wait(delay)
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
        ordered_array_len += 1
        pygame.time.wait(delay)

def merge(arr, start, end, mid):
    left = arr[start:mid+1]
    right = arr[mid+1:end+1]
    arr_ = arr[start:end+1]
    i, j, k = 0, 0, start
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            draw_merge_sort(arr, start, end,mid, i, j, k, arr_, left, right)
            pygame.time.wait(delay)
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            draw_merge_sort(arr, start, end,mid, i, j, k, arr_, left, right)
            pygame.time.wait(delay)
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        draw_merge_sort(arr, start, end,mid, i, j, k, arr_, left, right)
        pygame.time.wait(delay)
        i +=1
        k += 1
    while j < len(right):
        arr[k] = right[j]
        draw_merge_sort(arr, start, end,mid, i, j, k, arr_, left, right)
        pygame.time.wait(delay)
        j +=1
        k += 1
    draw_merge_sort(arr, start, end,mid, i, j, k, arr_, left, right)
    pygame.time.wait(delay)
    return arr
        

def merge_sort(arr, start, end):
    if end <= start:
        return arr
    mid  = start + (end-start)// 2
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)
    merge(arr, start, end, mid)
    return arr

def partition(arr, start, end):
    pivot_index = start
    pivot = arr[start]
    while start < end:
        while start < len(arr) and arr[start] <= pivot:
            draw_quick_sort(arr, start, end, pi=pivot_index)
            pygame.time.wait(delay)
            start += 1
        while arr[end] > pivot:
            draw_quick_sort(arr, start, end, pi=pivot_index)
            pygame.time.wait(delay)
            end -= 1
        if start < end:
            draw_quick_sort(arr, start, end, pi=pivot_index)
            pygame.time.wait(delay)
            arr[start], arr[end] = arr[end], arr[start]
    arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
    draw_quick_sort(arr, start, end, pi=pivot_index)
    pygame.time.wait(delay)
    return end

def quick_sort(arr, start, end):
    if start < end:
        pi = partition(arr, start, end)
        quick_sort(arr, start, pi-1)
        quick_sort(arr, pi + 1, end)
    return arr

running = True 
#t = time.time()
while running:
    clock.tick(24)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if sorted(arr) != arr:
            #arr = merge_sort(arr, 0, len(arr)-1)
            #selection_sort(arr)
            arr = quick_sort(arr, 0, len(arr)-1)
        else:
            #draw_merge_sort(arr,all_green=True)
            #draw_selection_sort(arr)
            draw_quick_sort(arr, all_green=True)
            #print(time.time()-t)
            #print(arr)
            #running = False
            #break





