# -*- coding: utf-8 -*-
from src.Types import DataType, RatingType, SecondQuantile, FirstQuantile, \
    ThirdQuantile
from src.QuantileRating import QuantileRating
import pytest


class TestQuantileRating:

    @pytest.fixture()
    def input_data(self) -> tuple[RatingType, dict[float, float]]:

        rating: RatingType = {
            "Иванов Иван Иванович": 82.0000,
            "Сидоров Витралий Павлович": 81.3333,
            "Богданова Анна Александровна": 73.6666,
            "Ежов Евгений Иванович": 64.6666,
        }

        quantiles = {
            FirstQuantile: 71.4166,
            SecondQuantile: 77.49995,
            ThirdQuantile: 81.49997499999999
        }

        return rating, quantiles

    def test_init_quantile_rating(self,
                                  input_data:
                                  tuple[RatingType, dict[float, float]]) \
            -> None:

        success_init_object = QuantileRating(input_data[0], FirstQuantile)

        assert isinstance(success_init_object, QuantileRating)

        with pytest.raises(Exception):
            QuantileRating(input_data[0], -2)

    def test_calc_quantile(self,
                           input_data:
                           tuple[RatingType, dict[float, float]]) -> None:

        for quantile in input_data[1]:
            quantile_rating = QuantileRating(input_data[0], quantile)
            assert pytest.approx(quantile_rating.quantile_calculated_value,
                                 abs=0.001) == input_data[1][quantile]

    def test_get_students_by_quantile(self,
                                      input_data:
                                      tuple[RatingType, dict[float, float]]) \
            -> None:
        for quantile in input_data[1]:
            quantile_rating = QuantileRating(input_data[0], quantile)

            quantile_students = \
                quantile_rating.get_students_by_quantile()
            for student in quantile_students:
                assert quantile_students[student] \
                       <= quantile_rating.quantile_calculated_value
