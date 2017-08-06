###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Jeremiah Flaga
# Collaborators:
# Time:
# Started coding:
# Finished coding, including tests:
#             A.1: Aug 6, 2017 10:05 PM - 10:25 PM
#             A.2: Aug 6, 2017 10:25 PM - 11:11 PM
#             A.3: Aug 6, 2017 11:27 PM - Aug 7, 2017 12:32 AM
#             A.4: Aug 7, 2017  2:30 AM -  2:40 AM
#             Also, I spent time fixing bug in my solution to A.3
#               - the bug was that I immediately returned the first partition that passes the constraint (limit)
#                   But it was not always the best partition


from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    dict = {}
    file = open(filename, 'r')
    for line in file:
        line = line.rstrip()
        if len(line) > 0:
            data = line.split(',')
            name = data[0]
            weight = int(data[1])
            dict[name] = weight

    file.close()
    return dict


# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    keys_sorted_by_weight = sorted(cows.keys(), key = lambda key: cows[key], reverse=True)
    cows_sorted = {}
    for key in keys_sorted_by_weight:
        cows_sorted[key] = cows[key]

    cows_for_all_trips = []
    while len(cows_sorted) > 0:
        cows_sorted_copy = cows_sorted.copy()
        available_weight_left = limit
        cows_for_this_trip = []

        for name in cows_sorted_copy.keys():
            weight = cows_sorted_copy[name]
            if weight <= available_weight_left:
                cows_for_this_trip.append(name)
                available_weight_left -= weight
                del(cows_sorted[name])

            if available_weight_left <= 0:
                break

        cows_for_all_trips.append(cows_for_this_trip)

    return cows_for_all_trips


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    names = cows.keys() # sorted(cows.keys(), key = lambda key: key)
    best_partition = names
    for partition in get_partitions(names):
        for list_of_names in partition:
            sum_of_weights = 0
            is_bad_partition = False
            for name in list_of_names:
                weight_of_current_cow = cows[name]
                sum_of_weights += weight_of_current_cow

            if sum_of_weights > limit:
                is_bad_partition = True
                break

        if not is_bad_partition and len(partition) < len(best_partition):
            best_partition = partition

    return best_partition
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    def print_results(filename):
        dict = load_cows(filename)
        print(filename)
        print()

        start = time.time()
        result = greedy_cow_transport(dict, 10)
        end = time.time()
        print('Greedy time (in seconds): {}'.format(end - start))
        print('Greedy result: ')
        print(result)

        print()

        start = time.time()
        result = brute_force_cow_transport(dict, 10)
        end = time.time()
        print('Brute Force time (in seconds): {}'.format(end - start))
        print('Brute Force result: ')
        print(result)

    print_results('ps1_cow_data.txt')
    print()
    print_results('ps1_cow_data_2.txt')


if __name__ == '__main__':
    compare_cow_transport_algorithms()

    
    # for partition in get_partitions([3, 1, 2]):
    #     print(partition)

    # dict = load_cows('ps1_cow_small_data_test.txt')
    # names = sorted(dict.keys(), key = lambda key: key)
    # print()
    # print(names)
    # for partition in get_partitions(names):
    #     print(partition)
        
    # brute_force_cow_transport(dict, 10)