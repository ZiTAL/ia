#!/usr/bin/python3
# -*- coding: utf-8 -*-
# pip3 install llama-cpp-python

import os, sys, re
from llama_cpp import Llama

dir   = os.path.dirname(os.path.abspath(sys.argv[0]))
files = sorted(list(filter(lambda file: re.match(r'^(.*?)\.bin$', file), os.listdir(dir))))

if(len(files)==0):
        print("First download models executing 'download.sh'")
        print("")
        sys.exit(1)

print("Model list:")
for i, file in enumerate(files):
        print(str(i+1)+": "+file)
index = input("Choose the model: (default: "+files[0]+") ")

try:
        index = int(index)
except:
        index = 1

index = index - 1

try:
        model = files[index]
except:
        model = files[0]

model = "./"+model

llm = Llama(
    model_path   = model,
    lora_path    = None,
    n_batch      = 512,
    n_ctx        = 1024,
    n_gpu_layers = 0,
    n_threads    = 3,
#    verbose      = True
    verbose      = False
)

while True:

    print("")
    print("Question: ")
#    print("")

    stream = llm(
        "### System: You are an AI assistant that follows instruction extremely well. Help as much as you can.\n\n### User: "+input()+"\n\n### Response: ",
        max_tokens=500,
        stop=["###"],
        stream=True,
        echo=True
    )

    for token in stream:
        print(token["choices"][0]["text"], end="", flush=True)
