import os
import json

class Convert:
    def __init__(self):
        self.json_path = './json'
        self.yolo_path = './yolo'
        self.class_path = './class.txt'
        self.class_list = self.class_load(self.class_path)

    def class_load(self, path):
        with open(self.class_path, 'r') as f:
            cl_list = f.readlines()
        cl_list = [line.rstrip('\n') for line in cl_list]
        return  cl_list

    def convert(self):
        print('Convet start')
        json_list = os.listdir(self.json_path)
        for obj in json_list:
            yolo_data = []
            file_num, a = obj.split('.')
            file_name = file_num + '.txt'

            with open(self.json_path + '/' + obj, "r") as json_file:
                json_data = json.load(json_file)
                for element in json_data:
                    yolo_data.append(self.class_list.index(element['class']))
                    yolo_data.append(element['position']['x'])
                    yolo_data.append(element['position']['y'])
                    yolo_data.append(element['position']['w'])
                    yolo_data.append(element['position']['h'])

            with open('yolo/'+file_name, 'w', encoding='UTF-8') as f:
                cnt = 0
                for el in yolo_data:
                    f.write(str(el))
                    cnt += 1
                    if cnt == 5:
                        f.write('\n')
                        cnt = 0
                    else:
                        f.write(' ')

        print('Convert end')


if __name__ == '__main__':
    Data = Convert()
    Data.convert()
