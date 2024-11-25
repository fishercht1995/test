from transformers import pipeline, AutoProcessor
import torch
import os
import time
import sys


st = time.time()
name = "Qwen2-VL-7B-Instruct"

if not os.path.exists(name):
    os.makedirs(name)



from transformers import Qwen2VLForConditionalGeneration, AutoTokenizer, AutoProcessor
from qwen_vl_utils import process_vision_info

# default: Load the model on the available device(s)
model = Qwen2VLForConditionalGeneration.from_pretrained(
    "Qwen/Qwen2-VL-7B-Instruct", torch_dtype="auto", device_map="auto",cache_dir=name
)
processor = AutoProcessor.from_pretrained("Qwen/Qwen2-VL-7B-Instruct",cache_dir=name)

print("{} {}".format(name, time.time() - st))



if sys.argv[1] == "1":
    if len(sys.argv) > 2:
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, sys.argv[2], name))
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, sys.argv[3], name))
    else:
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, "east1model", name))
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, "west1model", name))

os.system("rm -rf {}".format(name))