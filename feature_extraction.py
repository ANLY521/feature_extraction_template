#!/usr/bin/env python
import argparse
import numpy as np
from util import load_function_words, load_reviews


def main(data_file, vocab_path):
    """extract function word features from a text file"""

    # load resources and text file
    function_words = load_function_words(vocab_path)

    reviews, ids = load_reviews(data_file)


    # TODO 0: appropriately shape and fill this matrix
    review_features = np.zeros((1,1), dtype=np.int)
    # row is which review
    # column is which word

    print(f"Numpy array has shape {review_features.shape} and dtype {review_features.dtype}")

    # TODO 1: Figure out what the most common word (feature) is in review_features. Do not hardcode the answer
    most_common_count = 0
    most_common_word = ""
    print(f"Most common word: {most_common_word}, count: {most_common_count}")

    # TODO 2: Find any features that weren't in the data (i.e. columns that sum to 0)
    zero_inds = []
    if len(zero_inds)>0:
        print("No instances found for: ")
        for ind in zero_inds:
            print(f"  {function_words[ind]}")
    else:
        print("All function words found")


    matrix_sum = review_features.sum()
    print(f"Sum of raw count matrix: {matrix_sum}")

    # TODO 1: make a binary feature vector from your count vector
    word_binary = np.copy(review_features)
    word_binary_sum = word_binary.sum()
    print(f"1: Sum of binary matrix: {word_binary_sum}")

    # TODO 2: normalize features for review length (divide rows by number of *function words* in the review)
    # HINT: each row should sum to 1
    norm_reviews = np.copy(review_features)
    norm_reviews_sum = norm_reviews.sum()
    print(f"2: Sum of normed matrix: {norm_reviews_sum}")

    # TODO 3: remove features from <review_features> that occur less than <min_count> times
    min_count = 100
    min_matrix = np.copy(review_features)
    min_matrix_shape = min_matrix.shape
    print(f"3: Shape after removing features that occur < {min_count} times: {min_matrix_shape}")

    # TODO 4: normalize features by each feature's *document frequency*
    # For THIS exercise, divide each count by the number of documents that has that feature at all
    # (be careful not to divide by *total count* of the feature)
    # perform this on the matrix from TODO 3
    df_norm_reviews = np.copy(review_features)
    df_norm_reviews_sum = df_norm_reviews.sum()
    print(f"4: Sum of document frequency normed matrix: {df_norm_reviews_sum}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='feature vector homework')
    parser.add_argument('--path', type=str, default="imdb_practice.txt",
                        help='path to input with one review per line')
    parser.add_argument('--function_words_path', type=str, default="ewl_function_words.txt",
                        help='path to the list of words to use as features')
    args = parser.parse_args()

    main(args.path, args.function_words_path)
