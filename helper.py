import json

file = open("config/config.json", "r")

class help:

    def __init__(self):
        pass


    def load_config(self):
        try:
            json_file = file.read()
            confs = json.loads(str(json_file))
            return confs

        except Exception as e:
            print("JSON Load Error")
            print(e)


    def parse_params(self, params):
        try:
            conf = json.dumps(params)
            confs = json.loads(conf)
            return confs

        except Exception as e:
            print("JSON Load Error")
            print(e)