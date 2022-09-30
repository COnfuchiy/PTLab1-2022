# -*- coding: utf-8 -*-
import os.path
from typing import Any

import yaml

from Types import DataType
from abc import ABC

from DataReader import DataReader


def check_file(path: str):
    if not os.path.exists(path):
        raise OSError(path + " not exist")
    if not os.path.isfile(path):
        raise OSError(path + " not a file")


class YamlDataReader(DataReader, ABC):

    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        check_file(path)
        with open(path, "r", encoding='utf-8') as stream:
            data = yaml.safe_load(stream)
        self.init_students_data_from_yaml(data)
        return self.students

    def init_students_data_from_yaml(self, data: Any) -> None:
        for node in data:
            if not isinstance(node, dict):
                raise Exception("Invalid data file format")
            for fio in node:
                if isinstance(fio, str):
                    self.students[fio] = []
                    for subject in node[fio]:
                        if not isinstance(subject, str) and not isinstance(node[fio][subject], int):
                            raise Exception("Invalid data file format")
                        self.students[fio].append((subject, int(node[fio][subject])))
                else:
                    raise Exception("Invalid data file format")
