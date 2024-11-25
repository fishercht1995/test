from transformers import LlavaNextProcessor, LlavaNextForConditionalGeneration
import torch
import os
import time
import sys

st = time.time()
name = "llava-v1.6-mistral-7b-hf"

if not os.path.exists(name):
    os.makedirs(name)
name = "llava-v1.6-mistral-7b-hf"



processor = LlavaNextProcessor.from_pretrained("llava-hf/llava-v1.6-mistral-7b-hf", cache_dir=name)
model = LlavaNextForConditionalGeneration.from_pretrained("llava-hf/llava-v1.6-mistral-7b-hf", torch_dtype=torch.float16, low_cpu_mem_usage=True, cache_dir=name) 

print("{} {}".format(name, time.time() - st))



if sys.argv[1] == 1:
    if len(sys.argv) == 2:
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, sys.argv[2], name))
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, sys.argv[3], name))
    else:
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, "east1model", name))
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, "west1model", name))

os.system("rm -rf {}".format(name))