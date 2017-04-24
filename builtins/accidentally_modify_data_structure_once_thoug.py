# accidentally_modifying_data_structure_once_thought_was_fixed.py

def totally_innocent_function(movie_list):
    movie_list.append('You Got Served')

the_best_movies_of_all_time = ['The Godfather', 'Citizen Kane', '2001: A Space Odyssey']
print(the_best_movies_of_all_time)
totally_innocent_function(the_best_movies_of_all_time)
print(the_best_movies_of_all_time)