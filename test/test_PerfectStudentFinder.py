# -*- coding: utf-8 -*-
import pytest
from src.Types import DataType
from src.PerfectStudentFinder import PerfectStudentFinder

class TestPerfectStudentFinder:
    @pytest.fixture()
    def perfect_student_data(self) -> DataType:
        return {
            "Иванов Иван": [
                ("математика", 100),
                ("физика", 100)
            ],
            "Петров Петр": [
                ("математика", 90),
                ("физика", 100)
            ],
            "Сидоров Алексей": [
                ("химия", 100),
                ("биология", 100),
                ("физика", 100)
            ]
        }
    
    @pytest.fixture()
    def no_perfect_student_data(self) -> DataType:
        return {
            "Иванов Иван": [
                ("математика", 99),
                ("физика", 100)
            ],
            "Петров Петр": [
                ("математика", 90),
                ("физика", 85)
            ]
        }
    
    def test_find_perfect_student_exists(self, perfect_student_data: DataType) -> None:
        finder = PerfectStudentFinder(perfect_student_data)
        result = finder.find()
        # Должен найти первого совершенного студента
        assert result in ["Иванов Иван", "Сидоров Алексей"]
    
    def test_find_perfect_student_not_exists(self, no_perfect_student_data: DataType) -> None:
        finder = PerfectStudentFinder(no_perfect_student_data)
        result = finder.find()
        assert result == "Студентов с 100 баллами по всем предметам не найдено"