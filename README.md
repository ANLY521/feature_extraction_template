# Feature Extraction

Create and manipulate feature vectors from text using numpy.

It is possible to manipulate the matrices in this homework  using iteration, but numpy
provides more efficient methods - please use the numpy docs.

This homework practices:
* numpy arrays
* operations on arrays - entire array and only certain axes
* count vectors as features, binary vectors, normalized count vectors
* slicing arrays
* documentation - please update comments and docstrings and add to this README.md with a brief description


# Files

## imdb_practice.txt / imdb_grade.txt

TSV files of IMDB reviews used for debugging and grading.

## imdb_practice_result.txt

Desired output for `feature_extraction.py` on `imdb_practice.txt`. 

## util.py

Utility functions for data loading and splitting. 
Includes functions that must be completed for lab.

## lab.py

Creates feature vectors using function words in numpy.

Usage `python lab.py --path imdb_practice.txt`

## feature_extraction.py

This homework assignment practices creating feature vectors from text. 
Lowercase everything and use the `word_tokenize` function from `nltk` to tokenize.
The code runs but is missing the parts that fill the matrix and perform calculations on it, marked with TODO. 
Fill in the missing parts of the code as directed by the comments.

Do not alter the print statements - they are used for grading.
You can check your output for `imdb_practice.txt` against `imdb_practice_result.txt`.
For grading, your code will be run on a different data file in the same format and the print-out compared to
the correct results.

