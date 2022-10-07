import numpy

from Types import RatingType


class QuantileRating:

    def __init__(self, rating: RatingType) -> None:
        self.rating = rating
        self.quantile_calculated_values: list = []
        self.calc_quantiles()

    def calc_quantiles(self):
        rating_list = list(self.rating.values())
        self.quantile_calculated_values.append(
            numpy.quantile(rating_list, 0.25)
        )
        self.quantile_calculated_values.append(
            numpy.quantile(rating_list, 0.5)
        )

    def get_students_by_quartile(self) -> RatingType:
        output_students: RatingType = {}

        for student in self.rating:
            if self.quantile_calculated_values[0] <= self.rating[student] <= \
                    self.quantile_calculated_values[1]:
                output_students[student] = self.rating[student]

        return output_students
