from movie.movie_services import movie_service
from movie.utility import constant, print_util, input_util, menu_util
from movie.utility.input_util import please_enter_to_continue
from movie.utility.print_util import print_movie_list, print_stats_movies, \
    print_movie_does_not_exist, clear_menu


def list_movies_controller() -> None:
    result = movie_service.service_list_movies("",
                                               constant.PRODUCTION_FILE_PATH)
    print_movie_list(len(result[constant.PAYLOAD]), result[constant.PAYLOAD])

    please_enter_to_continue()

    menu_util.select_options(menu_util.call_menu())


def stats_movies_controller():
    result = movie_service.service_stat_movies(constant.PRODUCTION_FILE_PATH)
    print_stats_movies(result[constant.PAYLOAD][0],
                       result[constant.PAYLOAD][1],
                       result[constant.PAYLOAD][2],
                       result[constant.PAYLOAD][3],
                       result[constant.PAYLOAD][4])

    clear_menu()


def generate_random_movie_controller():
    result = movie_service.service_random_movie(constant.PRODUCTION_FILE_PATH)

    print_util.print_random_generated_movie(result)


def add_movie_controller():
    try:
        movie_name, movie_year, movie_rating = input_util.input_add_movie()

        result = movie_service.service_add_movie(movie_name, movie_year,
                                                 movie_rating,
                                                 constant.PRODUCTION_FILE_PATH)
        if result["result"]:
            print(f"Movie {movie_name} successfully added")

    except Exception:
        print(f"Movie {movie_name} was not added")
    finally:
        clear_menu()


def update_movie_controller():
    while True:
        try:
            movie_name = input_util.input_update_movie()

            result = movie_service.service_find_movie(True, movie_name,
                                                      constant.PRODUCTION_FILE_PATH)
            if not result[constant.RESULT]:
                raise KeyError()

            movie_rating = input("Enter new movie rating: ")

            result_update = (movie_service.service_update_movie
                             (movie_name, movie_rating,
                              constant.PRODUCTION_FILE_PATH))

            if not result_update[constant.RESULT]:
                raise Exception()

            if result["result"]:
                print(f"Movie {movie_name} successfully updated")

        except KeyError:
            print_movie_does_not_exist(movie_name)
        except Exception:
            print(f"Movie {movie_name} was not updated")
        finally:
            break
    clear_menu()


def delete_movie_controller():
    while True:
        try:
            movie_name = input_util.input_delete_movie()

            result = (movie_service.service_delete_movie
                      (movie_name, constant.PRODUCTION_FILE_PATH))

            if not result[constant.RESULT]:
                raise KeyError()

            if result["result"]:
                print(f"Movie {movie_name} successfully deleted")

        except KeyError:
            print_movie_does_not_exist(movie_name)

        except Exception:
            print(f"Movie {movie_name} was not deleted")

        finally:
            break

    clear_menu()


def search_movie_controller():
    part_movie_name = input_util.input_search_movie()

    result = movie_service.service_find_movie(part_movie_name,
                                              constant.PRODUCTION_FILE_PATH)

    print_util.print_movie_search(result[constant.PAYLOAD])
