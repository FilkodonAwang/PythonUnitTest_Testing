import yaml
import requests
import json
import unittest
from pydoc import locate


class Test_POSTS_API_DETAILS(unittest.TestCase):


    def read_yaml(self):
        import os
        try:
            print(os.getcwd())
            with open("./common.yaml",'r') as stream:
                try:
                    return yaml.safe_load(stream)
                except yaml.YAMLError as exc :
                    pass
        except:
            print(os.getcwd)


    def setUp(self):
        self.yaml_data = self.read_yaml()
        self.cmd = str(self.yaml_data["variables"]["data"]["url"])+"/"+str(self.yaml_data["variables"]["data"]["query"]["name"])+"/"+str(self.yaml_data["variables"]["data"]["query"]["id"])+"?"+str(self.yaml_data["variables"]["data"]["query"]["selector"]+"="+str(self.yaml_data["variables"]["data"]["query"]["selector_value"]))
        self.response = requests.get(self.cmd)
        self.assertEqual(int(self.response.status_code), 200)
        self.data = json.loads(self.response.text)
        self.processing_field = self.data[str(self.yaml_data["variables"]["data"]["check"]["name"])]
        self.expected_type = locate(str(self.yaml_data["variables"]["data"]["check"]["expected_type"]))

    def test_data_type_check(self):
        self.assertTrue(type(self.processing_field) is self.expected_type)

    def test_data_value_valide(self):
        field_type = type(self.processing_field)
        if field_type is str:
            self.assertTrue(len(self.processing_field) > 0)
        elif field_type is int:
            self.assertTrue(self.processing_field > 0)





if __name__ == '__main__':
    unittest.main()

