import pygame

from DrawInformation import DrawInformation
from utilities import draw_list, draw, generate_starting_list
import sorting_algorithms

def main():
    """
    Driver code
    :return: None
    """
    run = True

    clock = pygame.time.Clock()
    n = 50
    min_val = 0
    max_val = 100
    array = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, array)
    sorting = False
    ascending = True

    sorting_algorithm = sorting_algorithms.bubble_sort
    sorting_algo_name = "Bubble Sort"
    sorting_algorithm_generator = None
    fps = 60
    while run:
        clock.tick(fps)
        if sorting:
            try:
                next(sorting_algorithm_generator)
            except StopIteration:
                sorting = False
        else:
            draw(draw_info, sorting_algo_name, ascending, fps)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type != pygame.KEYDOWN:
                continue
            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_i and not sorting:
                sorting_algo_name = "Insertion Sort"
                sorting_algorithm = sorting_algorithms.insertion_sort
            elif event.key == pygame.K_b and not sorting:
                sorting_algo_name = "Bubble Sort"
                sorting_algorithm = sorting_algorithms.bubble_sort
            elif event.key == pygame.K_m and not sorting:
                sorting_algo_name = "Merge Sort"
                sorting_algorithm = sorting_algorithms.merge_sort
            elif event.key == pygame.K_q and not sorting:
                sorting_algo_name = "Quick Sort"
                sorting_algorithm = sorting_algorithms.quick_sort
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_RIGHT and not sorting:
                fps += 1
            elif event.key == pygame.K_LEFT and not sorting:
                fps -= 1

    pygame.quit()


if __name__ == "__main__":
    main()
