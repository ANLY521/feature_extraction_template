#!/usr/bin/env python
import argparse
from util import load_reviews, shuffle_dataset
import numpy as np


def main(data_file):
    """extract function word features from a text file"""

    # TODO: parse the review file. Field [0] per line is the review ID. Field[-1] is the review
    # define this function in util.py
    reviews, ids = load_reviews(data_file)

    # debug using just a few
    reviews = reviews[:10]

    feature_key = ["the", "or", "and"]

    print(f"loading feature vectors for {len(reviews)} reviews")

    # TODO: For function words "the", "or" and "and", use a Python list to
    #     make a count vector per review
    feature_lists = []

    # TODO: Create the same feature vectors as a numpy array
    feature_np = np.zeros(((len(reviews)), len(feature_key)), dtype=np.int)

    # Verify your list and numpy array are the same result
    are_equal = np.array_equal(np.asarray(feature_lists), feature_np)
    if are_equal:
        print("Numpy and list reprs are the same!")
    else:
        print("Numpy and list reprs are not equivalent. Keep trying!")

    # TODO: Calculate the total count per feature using your np array and .sum
    count_per_feat = [0,0,0]

    for i, feature_name in enumerate(feature_key):
        print(f"Count of '{feature_name}': {count_per_feat[i]}")





if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='feature vector lab')
    parser.add_argument('--path', type=str, default="imdb_practice.txt",
                        help='path to input with one review per line')

    args = parser.parse_args()

    main(args.path)
