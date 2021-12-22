import pygame

from DrawInformation import DrawInformation
from utilities import draw_list, draw, generate_starting_list
import sorting_algorithms as sa

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
    draw_info = DrawInformation(1280, 720, array)
    sorting = False
    ascending = True

    algo_list = sa.AlgorithmList({
        "Bubble Sort": sa.bubble_sort,
        "Insertion Sort": sa.insertion_sort,
        "Quick Sort": sa.quick_sort,
        "Merge Sort": sa.merge_sort,
    })

    sorting_algo_name, sorting_algorithm = algo_list.get_current_algo()
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
                array = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(array)
                sorting = False
            elif event.key == pygame.K_SPACE and not sorting:
                sorting = True
                sorting_algorithm_generator = sorting_algorithm(draw_info, ascending)
            elif event.key == pygame.K_s:
                sorting_algo_name, sorting_algorithm = algo_list.back()
            elif event.key == pygame.K_w:
                sorting_algo_name, sorting_algorithm = algo_list.next()
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False
            elif event.key == pygame.K_UP and not sorting:
                next_size = n + 30
                if 50 <= next_size <= 200:
                    n = next_size
                    max_val += 30
                    new_array = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(new_array)
            elif event.key == pygame.K_DOWN and not sorting:
                next_size = n - 30
                if 50 <= next_size <= 200:
                    n = next_size
                    max_val -= 30
                    new_array = generate_starting_list(n, min_val, max_val)
                    draw_info.set_list(new_array)
            elif event.key == pygame.K_RIGHT and not sorting:
                new_fps = fps + 1
                if new_fps <= 60:
                    fps = new_fps
            elif event.key == pygame.K_LEFT and not sorting:
                new_fps = fps - 1
                if 1 <= new_fps:
                    fps = new_fps

    pygame.quit()


if __name__ == "__main__":
    main()
