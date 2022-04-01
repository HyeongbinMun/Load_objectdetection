import os

class Pairing:
    def __init__(self):
        self.json_path = './json'
        self.image_path = './image'

    def file_sort(self):
        json_list = os.listdir(self.json_path)
        image_list = os.listdir(self.image_path)
        for image in image_list:
            check = 0
            image_num, a = image.split('.')
            for json in json_list:
                json_num, b = json.split('.')
                if image_num == json_num:
                    check += 1

            if check != 1:
                os.remove(self.image_path + '/' + image)

if __name__ == '__main__':
    file_pair = Pairing()
    file_pair.file_sort()