from transformers import pipeline, AutoProcessor
import torch
import os
import time
import sys


st = time.time()
name = "paligemma-3b-mix-224"

if not os.path.exists(name):
    os.makedirs(name)



from transformers import AutoProcessor, PaliGemmaForConditionalGeneration

model_id = "google/paligemma-3b-mix-224"

model = PaliGemmaForConditionalGeneration.from_pretrained(model_id, cache_dir=name)
processor = AutoProcessor.from_pretrained(model_id,cache_dir=name)
print("{} {}".format(name, time.time() - st))



if sys.argv[1] == "1":
    if len(sys.argv) > 2:
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, sys.argv[2], name))
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, sys.argv[3], name))
    else:
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, "east1model", name))
        os.system("aws s3 cp {} s3://{}/{} --recursive".format(name, "west1model", name))

os.system("rm -rf {}".format(name))