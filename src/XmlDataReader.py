# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from Types import DataType
from DataReader import DataReader

class XmlDataReader(DataReader):
    def read(self, path: str) -> DataType:
        """
        Чтение данных из XML-файла
        """
        students = {}
        
        # Парсим XML-файл
        tree = ET.parse(path)
        root = tree.getroot()
        
        # Проходим по всем студентам
        for student_elem in root.findall('student'):
            name = student_elem.find('name').text.strip()
            students[name] = []
            
            # Проходим по всем предметам студента
            subjects_elem = student_elem.find('subjects')
            for subject_elem in subjects_elem.findall('subject'):
                subject_name = subject_elem.find('name').text.strip()
                grade = int(subject_elem.find('grade').text.strip())
                students[name].append((subject_name, grade))
                
        return students