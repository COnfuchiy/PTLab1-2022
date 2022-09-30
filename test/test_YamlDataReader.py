# -*- coding: utf-8 -*-
from typing import Any

import pytest
import yaml

from YamlDataReader import YamlDataReader, check_file
from src.Types import DataType


class TestYamlDataReader:

    @pytest.fixture()
    def invalid_filepath(self) -> str:
        return "/fff/data.yaml"

    @pytest.fixture()
    def invalid_file_content(self) -> str:
        return "- Иванов Константин Дмитриевич: математика: 80\n" + \
               "математика: 91\n" + "    химия: 100\n" + \
               "- Петров Петр Семенович\n" + \
               "    русский язык: 87\n" + "    литература: 78\n"

    @pytest.fixture()
    def invalid_data_content(self) -> Any:
        return {
            "Иванов Константин Дмитриевич": "литература",
            "Петров Петр Семенович": [
                (5436, 7823)
            ]
        }

    @pytest.fixture()
    def valid_file_and_data_content(self) -> tuple[str, DataType]:
        yaml_text = "- Иванов Константин Дмитриевич:\n" + \
               "    математика: 91\n" + "    химия: 100\n" + \
               "- Петров Петр Семенович:\n" + \
               "    русский язык: 87\n" + "    литература: 78\n"

        data = {
            "Иванов Константин Дмитриевич": [
                ("математика", 91), ("химия", 100)
            ],
            "Петров Петр Семенович": [
                ("русский язык", 87), ("литература", 78)
            ]
        }
        return yaml_text, data

    @pytest.fixture()
    def valid_filepath_and_data(self,
                                valid_file_and_data_content: tuple[str, DataType],
                                tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("valid_data_dir").join("valid_test_data.yaml")
        p.write_text(valid_file_and_data_content[0], encoding='utf-8')
        return str(p), valid_file_and_data_content[1]

    @pytest.fixture()
    def invalid_filepath_and_data(self,
                                invalid_file_content: str,
                                invalid_data_content: Any,
                                tmpdir) -> tuple[str, Any]:
        p = tmpdir.mkdir("invalid_data_dir").join("invalid_test_data.yaml")
        p.write_text(invalid_file_content, encoding='utf-8')
        return str(p), invalid_data_content

    def test_read(self, valid_filepath_and_data: tuple[str, DataType], invalid_filepath_and_data: tuple[str, Any], invalid_data_content: Any,) -> None:
        file_content = YamlDataReader().read(valid_filepath_and_data[0])
        assert file_content == valid_filepath_and_data[1]

        yaml_data_reader = YamlDataReader()

        with pytest.raises(yaml.YAMLError):
            yaml_data_reader.read(invalid_filepath_and_data[0])

        with pytest.raises(Exception):
            yaml_data_reader.init_students_data_from_yaml(invalid_filepath_and_data[1])


    def test_check_file(self, valid_filepath_and_data, invalid_filepath: str, tmpdir) -> None:
        with pytest.raises(OSError):
            check_file(invalid_filepath)
        with pytest.raises(OSError):
            check_file(str(tmpdir))

        assert check_file(valid_filepath_and_data[0]) is None
