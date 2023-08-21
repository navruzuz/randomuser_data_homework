import json

def get_data(filename:str) -> dict:
#     """
#     You are given a filename. Read the JSON data from the file and return the dictionary.

#     Args:
#         filename(str): file name
#     Returns:
#         dict: JSON data
#     """
    f=open('data.json','r')
    data_json=f.read()
    data=json.loads(data_json)
    file_path=json.loads(data)
    print(get_data(file_path))