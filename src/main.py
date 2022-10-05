# -*- coding: utf-8 -*-
import argparse
import sys

from CalcRating import CalcRating
from QuantileRating import QuantileRating
from Types import SecondQuantile
from YamlDataReader import YamlDataReader


def get_path_from_arguments(args) -> str:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                        help="Path to datafile")
    args = parser.parse_args(args)
    return args.path


def main():
    path = get_path_from_arguments(sys.argv[1:])

    reader = YamlDataReader()
    students = reader.read(path)
    print("Students: ", students)

    rating = CalcRating(students).calc()
    print("Rating: ", rating)

    quantile_rating = QuantileRating(rating, SecondQuantile). \
        get_students_by_quantile(ge=True)
    print("Second quantile students rating: ", quantile_rating)


if __name__ == "__main__":
    main()
