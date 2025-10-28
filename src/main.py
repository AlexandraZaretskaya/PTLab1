# -*- coding: utf-8 -*-
import argparse
import sys
from CalcRating import CalcRating
from TextDataReader import TextDataReader
from XmlDataReader import XmlDataReader
from PerfectStudentFinder import PerfectStudentFinder

def get_path_from_arguments(args) -> tuple[str, str]:
    parser = argparse.ArgumentParser(description="Path to datafile")
    parser.add_argument("-p", dest="path", type=str, required=True,
                      help="Path to datafile")
    parser.add_argument("-f", dest="format", type=str, default="txt",
                      help="File format: txt or xml")
    args = parser.parse_args(args)
    return args.path, args.format

def main():
    path, file_format = get_path_from_arguments(sys.argv[1:])
    
    # Выбираем подходящий ридер в зависимости от формата
    if file_format == "xml":
        reader = XmlDataReader()
    else:
        reader = TextDataReader()
        
    students = reader.read(path)
    print("Students: ", students)
    
    # Расчет рейтинга
    rating = CalcRating(students).calc()
    print("Rating: ", rating)
    
    # Поиск идеального студента (ваше задание)
    perfect_finder = PerfectStudentFinder(students)
    perfect_student = perfect_finder.find()
    print("Perfect student: ", perfect_student)

if __name__ == "__main__":
    main()