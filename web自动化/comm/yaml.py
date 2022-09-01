import os
import yaml

class Yamlutil:
    #读取extract文件
    def read_extract_yaml(self,key):
        with open(os.getcwd()+"./extract.yaml",mode="r",encoding="utf-8") as f:
            value=yaml.load(stream=f,Loader=yaml.FullLoader)
            return value[key];
    #写入extract文件
    def write_extract_yaml(self,data):
        with open(os.getcwd() + "./extract.yaml", mode="a", encoding="utf-8") as f:
            yaml.dump(data=data,stream=f,allow_unicode=True )
    #清除extract文件
    def clear_extract_yaml(self):
        with open(os.getcwd() + "./extract.yaml", mode="w", encoding="utf-8") as f:
            f.truncate()
    #读取测试用例
    def read_case_yaml(self,yaml_name):
        with open(os.path.dirname(os.getcwd())+"/data/"+yaml_name,mode='r',encoding='utf-8') as f:
            valure=yaml.load(stream=f,Loader=yaml.FullLoader)
            return valure;