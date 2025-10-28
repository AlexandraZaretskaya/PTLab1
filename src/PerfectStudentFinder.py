# -*- coding: utf-8 -*-
from Types import DataType

class PerfectStudentFinder:
    def __init__(self, data: DataType) -> None:
        self.data: DataType = data
    
    def find(self) -> str:
        """
        Находит студента с 100 баллами по всем предметам
        Возвращает имя студента или сообщение об отсутствии
        """
        perfect_students = []
        
        for student_name, subjects in self.data.items():
            # Проверяем, все ли оценки = 100
            all_perfect = all(grade == 100 for _, grade in subjects)
            if all_perfect:
                perfect_students.append(student_name)
        
        if perfect_students:
            # Возвращаем первого найденного отличника
            return perfect_students[0]
        else:
            return "Студентов с 100 баллами по всем предметам не найдено"