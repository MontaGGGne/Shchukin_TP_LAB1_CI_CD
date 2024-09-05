# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from DataReader import DataReader
from Types import DataType


class XMLDataReader(DataReader):
    def __init__(self) -> None:
        self.students: DataType = {}

    def read(self, path: str) -> DataType:
        tree = ET.parse(path)
        root = tree.getroot()

        for student in root.findall('student'):
            student_name = student.get('name')
            self.students[student_name] = []

            for subject in student.findall('subject'):
                subj_name = subject.get('name')
                score = int(subject.get('score'))
                self.students[student_name].append((subj_name, score))

        return self.students
