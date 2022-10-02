import numpy

from Types import RatingType


class QuantileRating:

    def __init__(self, rating: RatingType, quantile: float) -> None:
        self.quantile_value: float = 0

        # quantile must be between 0 and 1 inclusive.
        # see https://numpy.org/doc/stable/reference/generated/numpy.quantile.html
        if not 0 <= quantile <= 1:
            raise Exception("Quantile must be between 0 and 1 inclusive")
        self.quantile_value = quantile
        self.rating = rating
        self.quantile_calculated_value: float = 0
        self.calc_quantile()

    def calc_quantile(self):
        rating_list = list(self.rating.values())
        self.quantile_calculated_value = numpy.quantile(rating_list, self.quantile_value)

    def get_students_by_quantile(self, ge:bool = True,le: bool = False)->RatingType:
        """
        :param ge: bool - greater than or equal to the quantile value
        :param le: bool - less than or equal to the quantile value
        :rtype: RatingType
        """
        output_students:RatingType = {}

        for student in self.rating:
            if ge and self.rating[student] >= self.quantile_calculated_value or \
                    le and self.rating[student] <= self.quantile_calculated_value:
                output_students[student] = self.rating[student]

        return output_students