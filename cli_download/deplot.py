from transformers import pipeline, AutoProcessor
import torch
import os
import time
import sys


st = time.time()
name = "deploy"

if not os.path.exists(name):
    os.makedirs(name)



from transformers import Pix2StructProcessor, Pix2StructForConditionalGeneration
processor = Pix2StructProcessor.from_pretrained('google/deplot',cache_dir=name)
model = Pix2StructForConditionalGeneration.from_pretrained('google/deplot',cache_dir=name)


print("{} {}".format(name, time.time() - st))



if sys.argv[1] == "1":
    if len(sys.argv) > 2:
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, sys.argv[2], name))
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, sys.argv[3], name))
    else:
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, "east1model", name))
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, "west1model", name))

os.system("rm -rf {}".format(name))