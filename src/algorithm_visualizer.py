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
        self.algorithm = "selection sort"

    def reset_arr(self):
        self.arr = [random.randint(-99,99) for _ in range(50)]
        self.sort = False

    def draw_menu(self):
        x, y = 0, 0
        width = self.screen.get_width()
        height = self.screen.get_height()
        menu_background = pygame.Rect(x, y, width, 3 * self.block_size)
        pygame.draw.rect(screen, GREY, menu_background, 0)

        reset_button = pygame.Rect(x + 1*self.block_size, y + 1*self.block_size, 2*self.block_size, self.block_size)
        play_button = pygame.Rect(width//4 + 1*self.block_size, y + 1*self.block_size, 2*self.block_size, self.block_size)
        selection_sort_button = pygame.Rect(width//2 + 1*self.block_size, y + 1*self.block_size, 5*self.block_size, self.block_size)
        merge_sort_button = pygame.Rect(width//2  + 7*self.block_size, y + 1*self.block_size, 5*self.block_size, self.block_size)
        quick_sort_button = pygame.Rect(width//2 + 13*self.block_size, y + 1*self.block_size, 5*self.block_size, self.block_size)

        pygame.draw.rect(screen, BACKGROUD_COLOUR, reset_button, 1, border_radius=3)
        pygame.draw.rect(screen, BACKGROUD_COLOUR, play_button, 1, border_radius=3)
        pygame.draw.rect(screen, BACKGROUD_COLOUR, selection_sort_button, 1, border_radius=3)
        pygame.draw.rect(screen, BACKGROUD_COLOUR, merge_sort_button, 1, border_radius=3)
        pygame.draw.rect(screen, BACKGROUD_COLOUR, quick_sort_button, 1, border_radius=3)

        text_rect = reset_button
        text = font.render(f"RESET", True, BACKGROUD_COLOUR)
        text_rect = text.get_rect()
        text_rect.center = reset_button.center
        screen.blit(text, text_rect)

        text_rect = play_button
        text = font.render(f"PLAY", True, BACKGROUD_COLOUR)
        text_rect = text.get_rect()
        text_rect.center = play_button.center
        screen.blit(text, text_rect)

        text_rect = selection_sort_button
        text = font.render(f"SELECTION SORT", True, BACKGROUD_COLOUR)
        text_rect = text.get_rect()
        text_rect.center = selection_sort_button.center
        screen.blit(text, text_rect)
 
        text_rect = merge_sort_button
        text = font.render(f"MERGE SORT", True, BACKGROUD_COLOUR)
        text_rect = text.get_rect()
        text_rect.center = merge_sort_button.center
        screen.blit(text, text_rect)
    
        text_rect = reset_button
        text = font.render(f"QUICK SORT", True, BACKGROUD_COLOUR)
        text_rect = text.get_rect()
        text_rect.center = quick_sort_button.center
        screen.blit(text, text_rect)
 
        pos = pygame.mouse.get_pos()
        if reset_button.collidepoint(pos):
            if pygame.mouse.get_pressed()[0]:
                self.reset_arr()
        if play_button.collidepoint(pos):
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
                        selection_sort(self.arr, delay=self.delay)
                    elif self.algorithm == "merge sort":
                        merge_sort(self.arr, 0, len(self.arr)-1, delay=self.delay)
                    else:
                        quick_sort(self.arr, 0, len(self.arr)-1, delay=self.delay)
                else:
                    draw_quick_sort(self.arr, all_green=True, delay=self.delay)
                    self.draw_menu()
            else:
                draw_quick_sort(self.arr, all_green=False, delay=self.delay)
                self.draw_menu()
            




def main():
    app = AlgorithmVisualizer(delay=10)
    app.run()

if __name__ == "__main__":
    main()