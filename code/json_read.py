import json

class Result:

    def __init__(self):
        self.json_path = 'labels.json'
        self.size = [960, 540]
        self.index = []
        self.count = 0

    def convert(self, x1, y1, x2, y2):
        dw = 1./self.size[0]
        dh = 1. / self.size[1]
        x = (float(x1) + float(x2)) / 2.0
        y = (float(y1) + float(y2)) / 2.0
        w = float(x2) - float(x1)
        h = float(y2) - float(y1)

        x = round(x * dw, 6)
        w = round(w * dw, 6)
        y = round(y * dh, 6)
        h = round(h * dh, 6)
        if w < 0 or h < 0:
            self.count += 1
            print(self.count)

        return x, y, w, h

    def write_data(self):
        with open(self.json_path, "r") as json_file:
            json_data = json.load(json_file)
            for el in json_data['annotations']:
                self.index.append(el)

        for el in self.index:
            obj_list = el['objects']
            obj_data = []

            for obj in obj_list:
                pos = obj['position']
                pos['x'], pos['y'], pos['w'], pos['h'] = self.convert(pos['xmin'], pos['ymin'], pos['xmax'], pos['ymax'])
                del pos['xmin'], pos['xmax'], pos['ymin'], pos['ymax']
                if self.count !=0:
                    print(el['file_name'])
                    self.count = 0

                obj['position'] = pos
                obj_data.append(obj)

            # with open('json/'+el['file_name'], 'w', encoding="utf-8") as make_file:
            #     json.dump(obj_data, make_file, ensure_ascii=False, indent='\t')


if __name__ == '__main__':
    result = Result()
    result.write_data()
