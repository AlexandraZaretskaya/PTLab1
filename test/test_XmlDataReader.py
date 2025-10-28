# -*- coding: utf-8 -*-
import pytest
import tempfile
import os
from src.Types import DataType
from src.XmlDataReader import XmlDataReader

class TestXmlDataReader:
    @pytest.fixture()
    def xml_content(self) -> str:
        return """<?xml version="1.0" encoding="UTF-8"?>
<students>
    <student>
        <name>Иванов Иван</name>
        <subjects>
            <subject>
                <name>математика</name>
                <grade>100</grade>
            </subject>
            <subject>
                <name>физика</name>
                <grade>90</grade>
            </subject>
        </subjects>
    </student>
</students>"""
    
    @pytest.fixture()
    def expected_data(self) -> DataType:
        return {
            "Иванов Иван": [
                ("математика", 100),
                ("физика", 90)
            ]
        }
    
    @pytest.fixture()
    def xml_file(self, xml_content: str) -> str:
        # Создаем временный XML-файл для тестов
        with tempfile.NamedTemporaryFile(mode='w', suffix='.xml', delete=False, encoding='utf-8') as f:
            f.write(xml_content)
            temp_path = f.name
        yield temp_path
        # Удаляем временный файл после теста
        os.unlink(temp_path)
    
    def test_read_xml(self, xml_file: str, expected_data: DataType) -> None:
        reader = XmlDataReader()
        data = reader.read(xml_file)
        assert data == expected_data