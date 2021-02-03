#!/usr/bin/env python
import numpy as np

def load_function_words(resource_path):
    """load a newline separated text file of function words.
    Return a list"""
    f_words = []
    with open(resource_path, 'r') as f:
        for line in f:
            if line.strip():
                f_words.append(line.lower().strip())
    return f_words

# TODO: write this function (lab)
def load_reviews(data_file):
    """
    Load a tsv of movie reviews, where field 0 is review id and field -1 is review
    :param data_file: data file path
    :return: two lists, (reviews, ids)
    """
    reviews = []
    ids = []
    return reviews,ids

# TODO: write this function (lab)
def shuffle_dataset(data, id_strs):
    """
    Shuffles a list of datapoints and their id's in unison
    :param data: iterable, each item a datapoint
    :param id_strs: iterable, each item an id
    :return: tuple (shuffled_data, shuffled_id_strs)
    """
    shuffled_ids = id_strs
    shuffled_data = data
    return (shuffled_data, shuffled_ids)
