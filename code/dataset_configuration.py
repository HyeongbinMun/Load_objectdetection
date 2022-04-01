import os
import shutil
# import splitfolders
#
# splitfolders.ratio('./data', output='yolo_data', seed=77, ratio=(.8, .2))

class Configuration:
    def __init__(self):
        self.train_path = './yolo_data/train'
        self.val_path = './yolo_data/val'
        self.yolo_path = './yolo'

    def configuration(self):
        train_list = os.listdir(self.train_path)
        val_list = os.listdir(self.val_path)
        yolo_list = os.listdir(self.yolo_path)
        for train_data in train_list:
            for yolo_data in yolo_list:
                train_num, a = train_data.split('.')
                yolo_num, b = yolo_data.split('.')
                if train_num == yolo_num:
                    shutil.copy(self.yolo_path + '/' + yolo_data, self.train_path + '/' + yolo_data)

        for val_data in val_list:
            for yolo_data in yolo_list:
                val_num, a = val_data.split('.')
                yolo_num, b = yolo_data.split('.')
                if val_num == yolo_num:
                    shutil.copy(self.yolo_path + '/' + yolo_data, self.val_path + '/' + yolo_data)


if __name__ == '__main__':
    Data = Configuration()
    Data.configuration()