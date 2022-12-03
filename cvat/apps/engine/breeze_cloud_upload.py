import boto3
import os
from os.path import exists


def get_file_paths(files):
    # format is [{'file': '/home/django/data/data/9/raw/faqbackground.jpg'}]
    print("hullo i'm printing")
    print(files)

#for api testing
def get_labels(labels):
    result=[]
    for label in labels.values():
        result.append(label["name"])
    return result

def get_labels_file(labels):
    # print("this is hopefully the project name")
    # print(labels) #<QuerySet [<Label: body>, <Label: face>, <Label: license plate>, <Label: vehicle>]>
    file=open('labels.txt','w')
    for label in labels.values():
        file.writelines(label["name"]+',')
        print(label["name"]) #{'id': 24, 'task_id': None, 'project_id': 3, 'name': 'body', 'color': '#6ec3c1', 'type': 'any', 'parent_id': None}
    file.close()

    print(exists('labels.txt'))

def connect_to_s3(dir_name):
    s3 = boto3.client("s3")
    d= dir_name.split('/')[-1]
    print(d)
    bucket = "label-cvat-storage"
    object_name = d+"/labels.txt"
    file_name = "labels.txt"
    print(file_name, bucket, object_name)
    response = s3.upload_file(file_name, bucket, object_name)
    print(response)



