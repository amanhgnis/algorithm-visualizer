import pygame
from consts import *
import random

class AlgorithmVisualizer:
    def __init__(self, width=1300, height=525, block_size=25, frame_rate=24, delay=50):
        pygame.init()
        pygame.display.set_caption("Algorithm Visualizer")
        self.clock = pygame.time.Clock()
        self.frame_rate = frame_rate
        self.delay = delay
        self.font = pygame.font.Font(None, 16)
        self.width, self.height, self.block_size = width, height, block_size
        self.screen = pygame.display.set_mode((self.width, self.height), pygame.RESIZABLE)
        self.running = True
        self.reset_arr()
        self.algorithm = "selection sort"

    def reset_arr(self):
        self.arr = [random.randint(0,99) for _ in range(50)]
        self.sort = False
        
    def draw_menu(self):
        x, y = 0, 0
        width = self.screen.get_width()
        height = self.screen.get_height()
        menu_background = pygame.Rect(x, y, width, 3 * self.block_size)
        pygame.draw.rect(self.screen, GREY, menu_background, 0)

        reset_button = pygame.Rect(x + 1*self.block_size, y + 1*self.block_size, 2*self.block_size, self.block_size)
        play_button = pygame.Rect(width//4 + 1*self.block_size, y + 1*self.block_size, 2*self.block_size, self.block_size)
        selection_sort_button = pygame.Rect(width//2 + 1*self.block_size, y + 1*self.block_size, 5*self.block_size, self.block_size)
        merge_sort_button = pygame.Rect(width//2  + 7*self.block_size, y + 1*self.block_size, 5*self.block_size, self.block_size)
        quick_sort_button = pygame.Rect(width//2 + 13*self.block_size, y + 1*self.block_size, 5*self.block_size, self.block_size)

        pygame.draw.rect(self.screen, BACKGROUD_COLOUR, reset_button, 1, border_radius=3)
        pygame.draw.rect(self.screen, BACKGROUD_COLOUR, play_button, 1, border_radius=3)
        if self.algorithm == "selection sort":
            pygame.draw.rect(self.screen, BLUE, selection_sort_button, 0, border_radius=3)
        else:
            pygame.draw.rect(self.screen, BACKGROUD_COLOUR, selection_sort_button, 1, border_radius=3)
        if self.algorithm == "merge sort":
            pygame.draw.rect(self.screen, BLUE, merge_sort_button, 0, border_radius=3)
        else:
            pygame.draw.rect(self.screen, BACKGROUD_COLOUR, merge_sort_button, 1, border_radius=3)
        if self.algorithm == "quick sort":
            pygame.draw.rect(self.screen, BLUE, quick_sort_button, 0, border_radius=3)
        else:
            pygame.draw.rect(self.screen, BACKGROUD_COLOUR, quick_sort_button, 1, border_radius=3)

        text_rect = reset_button
        text = self.font.render(f"RESET", True, BACKGROUD_COLOUR)
        text_rect = text.get_rect()
        text_rect.center = reset_button.center
        self.screen.blit(text, text_rect)

        text_rect = play_button
        text = self.font.render(f"PLAY", True, BACKGROUD_COLOUR)
        text_rect = text.get_rect()
        text_rect.center = play_button.center
        self.screen.blit(text, text_rect)

        text_rect = selection_sort_button
        text = self.font.render(f"SELECTION SORT", True, BACKGROUD_COLOUR)
        text_rect = text.get_rect()
        text_rect.center = selection_sort_button.center
        self.screen.blit(text, text_rect)
 
        text_rect = merge_sort_button
        text = self.font.render(f"MERGE SORT", True, BACKGROUD_COLOUR)
        text_rect = text.get_rect()
        text_rect.center = merge_sort_button.center
        self.screen.blit(text, text_rect)
    
        text_rect = reset_button
        text = self.font.render(f"QUICK SORT", True, BACKGROUD_COLOUR)
        text_rect = text.get_rect()
        text_rect.center = quick_sort_button.center
        self.screen.blit(text, text_rect)
 
        pos = pygame.mouse.get_pos()
        if reset_button.collidepoint(pos):
            pygame.draw.rect(self.screen, BACKGROUD_COLOUR, reset_button, 0, border_radius=3)
            text_rect = reset_button
            text = self.font.render(f"RESET", True, GREY)
            text_rect = text.get_rect()
            text_rect.center = reset_button.center
            self.screen.blit(text, text_rect)
            if pygame.mouse.get_pressed()[0]:
                self.reset_arr()
        if play_button.collidepoint(pos):
            pygame.draw.rect(self.screen, BACKGROUD_COLOUR, play_button, 0, border_radius=3)
            text_rect = play_button
            text = self.font.render(f"PLAY", True, GREY)
            text_rect = text.get_rect()
            text_rect.center = play_button.center
            self.screen.blit(text, text_rect)
            if pygame.mouse.get_pressed()[0]:
                self.sort = True
        if selection_sort_button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.algorithm = "selection sort"
        if merge_sort_button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.algorithm = "merge sort"
        if quick_sort_button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.algorithm = "quick sort"
        
        pygame.display.update()
        
    def draw_selection_sort(self, arr, order_array_len=0, i=-1, j=-1):
        self.screen.fill(BACKGROUD_COLOUR)
        index = 0
        for x in range(self.block_size, self.block_size*(len(arr)+1), self.block_size):
            y = self.screen.get_height() // 2 - 1*self.block_size
            rect = pygame.Rect(x, y, self.block_size, self.block_size)
            pheight = 0.05 * arr[index]*self.block_size
            prect = pygame.Rect(x, y-pheight, self.block_size, pheight)
            text_rect = rect
            if index < order_array_len:
                pygame.draw.rect(self.screen, GREEN, rect, 0)
                pygame.draw.rect(self.screen, GREEN, prect, 0)
            if index == i:
                pygame.draw.rect(self.screen, RED, rect, 0)
                pygame.draw.rect(self.screen, RED, prect, 0)
            if index == j:
                pygame.draw.rect(self.screen, BLUE, rect, 0)
                pygame.draw.rect(self.screen, BLUE, prect, 0)
            pygame.draw.rect(self.screen, BLACK, rect, 1)
            pygame.draw.rect(self.screen, BLACK, prect, 1)
            text = self.font.render(f"{arr[index]}", True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = rect.center
            self.screen.blit(text, text_rect)
            index += 1
        pygame.display.update()

    def draw_merge_sort(self, arr, start=0, end=0, mid=-1, i=-1, j=-1, k=-1, arr_=[], left=[], right=[], all_green=False):
        self.screen.fill(BACKGROUD_COLOUR)
        index = 0
        y = self.screen.get_height() // 2 - 1*self.block_size
        for x in range(self.block_size, self.block_size*(len(arr)+1), self.block_size):
            rect = pygame.Rect(x, y, self.block_size, self.block_size)
            pheight = 0.05 * arr[index]*self.block_size
            prect = pygame.Rect(x, y-pheight, self.block_size, pheight)
            text_rect = rect
            if not all_green:
                if index > end:
                    pygame.draw.rect(self.screen, GREY, rect, 0)
                    pygame.draw.rect(self.screen, GREY, prect, 0)
                if index < start:
                    pygame.draw.rect(self.screen, GREY, rect, 0)
                    pygame.draw.rect(self.screen, GREY, prect, 0)
            else:
                pygame.draw.rect(self.screen, GREEN, rect, 0)
                pygame.draw.rect(self.screen, GREEN, prect, 0)
            pygame.draw.rect(self.screen, BLACK, rect, 1)
            pygame.draw.rect(self.screen, BLACK, prect, 1)

            if (index < k  or index > end) or all_green:
                pygame.draw.rect(self.screen, BLACK, rect, 1)
                text = self.font.render(f"{arr[index]}", True, BLACK)
                text_rect = text.get_rect()
                text_rect.center = rect.center
                self.screen.blit(text, text_rect)
            index += 1

        


        index = 0
        for x in range(self.block_size, self.block_size*(len(arr_)+1), self.block_size):
            rect_below = pygame.Rect(x, y + 2*self.block_size, self.block_size, self.block_size)
            text_rect = rect_below 
            pygame.draw.rect(self.screen, BLACK, rect_below, 1)
            text = self.font.render(f"{arr_[index]}", True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = rect_below.center
            self.screen.blit(text, text_rect)
            index += 1


        left_text = pygame.Rect(self.block_size, y + 4*self.block_size, 4*self.block_size, self.block_size)
        text_rect = left_text
        text = self.font.render(f"LEFT SUBARRAY", True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = left_text.center
        self.screen.blit(text, text_rect)

        index = 0
        for x in range(self.block_size, self.block_size*(len(left)+1), self.block_size):
            rect_below = pygame.Rect(x + 5*self.block_size, y + 4*self.block_size, self.block_size, self.block_size)
            text_rect = rect_below 
            if index == i:
                pygame.draw.rect(self.screen, RED, rect_below, 0)

            pygame.draw.rect(self.screen, BLACK, rect_below, 1)
            text = self.font.render(f"{left[index]}", True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = rect_below.center
            self.screen.blit(text, text_rect)
            index += 1


        right_text = pygame.Rect(self.block_size, y + 6*self.block_size, 4*self.block_size, self.block_size)
        text_rect = right_text
        text = self.font.render(f"RIGHT SUBARRAY", True, BLACK)
        text_rect = text.get_rect()
        text_rect.center = right_text.center
        self.screen.blit(text, text_rect)


        index = 0
        for x in range(self.block_size, self.block_size*(len(right)+1), self.block_size):
            rect_below = pygame.Rect(x + 5*self.block_size, y + 6*self.block_size, self.block_size, self.block_size)
            text_rect = rect_below 
            if index == j:
                pygame.draw.rect(self.screen, BLUE, rect_below, 0)
            pygame.draw.rect(self.screen, BLACK, rect_below, 1)
            text = self.font.render(f"{right[index]}", True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = rect_below.center
            self.screen.blit(text, text_rect)
            index += 1

        pygame.display.update()

    def draw_quick_sort(self, arr, start=-1, end=-1, pi=-1, all_green=False):
        self.screen.fill(BACKGROUD_COLOUR)
        index = 0
        for x in range(self.block_size, self.block_size*(len(arr)+1), self.block_size):
            y = self.screen.get_height() // 2 - 1*self.block_size
            rect = pygame.Rect(x, y, self.block_size, self.block_size)
            pheight = 0.05 * arr[index]*self.block_size
            prect = pygame.Rect(x, y-pheight, self.block_size, pheight)
            text_rect = rect
            if not all_green:
                if index == start:
                    pygame.draw.rect(self.screen, RED, rect, 0)
                    pygame.draw.rect(self.screen, RED, prect, 0)
                if index == end:
                    pygame.draw.rect(self.screen, BLUE, rect, 0)
                    pygame.draw.rect(self.screen, BLUE, prect, 0)
                if index == pi:
                    pygame.draw.rect(self.screen, GREEN, rect, 0)
                    pygame.draw.rect(self.screen, GREEN, prect, 0)
            else:
                pygame.draw.rect(self.screen, GREEN, rect, 0)
                pygame.draw.rect(self.screen, GREEN, prect, 0)
            pygame.draw.rect(self.screen, BLACK, rect, 1)
            pygame.draw.rect(self.screen, BLACK, prect, 1)
            text = self.font.render(f"{arr[index]}", True, BLACK)
            text_rect = text.get_rect()
            text_rect.center = rect.center
            self.screen.blit(text, text_rect)
            index += 1
        pygame.display.update()

    def selection_sort(self, arr):
        ordered_array_len = 0
        for i in range(len(arr)):
            min_index = i
            for j in range(i+1, len(arr)):
                if arr[j] <= arr[min_index]:
                    min_index = j
                self.draw_selection_sort(arr, ordered_array_len,i, j)
                pygame.time.wait(self.delay)
            if min_index != i:
                arr[i], arr[min_index] = arr[min_index], arr[i]
            ordered_array_len += 1
            pygame.time.wait(self.delay)

    def merge(self, arr, start, end, mid):
        left = arr[start:mid+1]
        right = arr[mid+1:end+1]
        arr_ = arr[start:end+1]
        i, j, k = 0, 0, start
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                self.draw_merge_sort(arr, start, end,mid, i, j, k, arr_, left, right)
                pygame.time.wait(self.delay)
                i += 1
                k += 1
            else:
                arr[k] = right[j]
                self.draw_merge_sort(arr, start, end,mid, i, j, k, arr_, left, right)
                pygame.time.wait(self.delay)
                j += 1
                k += 1
        while i < len(left):
            arr[k] = left[i]
            self.draw_merge_sort(arr, start, end,mid, i, j, k, arr_, left, right)
            pygame.time.wait(self.delay)
            i +=1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            self.draw_merge_sort(arr, start, end,mid, i, j, k, arr_, left, right)
            pygame.time.wait(self.delay)
            j +=1
            k += 1
        self.draw_merge_sort(arr, start, end,mid, i, j, k, arr_, left, right)
        pygame.time.wait(self.delay)
        return arr
            
    def merge_sort(self, arr, start, end):
        if end <= start:
            return arr
        mid  = start + (end-start)// 2
        self.merge_sort(arr, start, mid)
        self.merge_sort(arr, mid+1, end)
        self.merge(arr, start, end, mid)
        return arr

    def partition(self, arr, start, end):
        pivot_index = start
        pivot = arr[start]
        while start < end:
            while start < len(arr) and arr[start] <= pivot:
                self.draw_quick_sort(arr, start, end, pi=pivot_index)
                pygame.time.wait(self.delay)
                start += 1
            while arr[end] > pivot:
                self.draw_quick_sort(arr, start, end, pi=pivot_index)
                pygame.time.wait(self.delay)
                end -= 1
            if start < end:
                self.draw_quick_sort(arr, start, end, pi=pivot_index)
                pygame.time.wait(self.delay)
                arr[start], arr[end] = arr[end], arr[start]
        arr[pivot_index], arr[end] = arr[end], arr[pivot_index]
        self.draw_quick_sort(arr, start, end, pi=pivot_index)
        pygame.time.wait(self.delay)
        return end

    def quick_sort(self, arr, start, end):
        if start < end:
            pi = self.partition(arr, start, end)
            self.quick_sort(arr, start, pi-1)
            self.quick_sort(arr, pi + 1, end)
        return arr

    def run(self):
        while self.running:
            self.clock.tick(self.frame_rate)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.reset_arr()
                    if event.key == pygame.K_SPACE:
                        self.sort = True
                    if event.key == pygame.K_s:
                        self.algorithm = "selection sort"
                    if event.key == pygame.K_m:
                        self.algorithm = "merge sort"
                    if event.key == pygame.K_q:
                        self.algorithm = "quick sort"
            if self.sort:
                if sorted(self.arr) != self.arr:
                    if self.algorithm == "selection sort":
                        self.selection_sort(self.arr)
                    elif self.algorithm == "merge sort":
                        self.merge_sort(self.arr, 0, len(self.arr)-1)
                    else:
                        self.quick_sort(self.arr, 0, len(self.arr)-1)
                else:
                    self.draw_quick_sort(self.arr, all_green=True)
                    self.draw_menu()
            else:
                self.draw_quick_sort(self.arr, all_green=False)
                self.draw_menu()


def main():
    app = AlgorithmVisualizer(delay=25)
    app.run()

if __name__ == "__main__":
    main()