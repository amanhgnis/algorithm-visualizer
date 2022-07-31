import pygame
from consts import *
from algorithms import *
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

    def reset_arr(self):
        self.arr = [random.randint(-99,99) for _ in range(50)]
        self.sort = False

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
                        algorithm = "selection sort"
                    if event.key == pygame.K_m:
                        algorithm = "merge sort"
                    if event.key == pygame.K_q:
                        algorithm = "quick sort"
            if self.sort:
                if sorted(self.arr) != self.arr:
                    if algorithm == "selection sort":
                        selection_sort(self.arr, delay=self.delay)
                    elif algorithm == "merge sort":
                        merge_sort(self.arr, 0, len(self.arr)-1, delay=self.delay)
                    else:
                        quick_sort(self.arr, 0, len(self.arr)-1, delay=self.delay)
                else:
                    draw_quick_sort(self.arr, all_green=True, delay=self.delay)
            else:
                draw_quick_sort(self.arr, all_green=False, delay=self.delay)




def main():
    app = AlgorithmVisualizer(delay=10)
    app.run()

if __name__ == "__main__":
    main()