# ia
Inteligentzia artifiziala

# install
```
pip3 install llama-cpp-python
pip3 install llama-cpp-python[server]
```

# download models
```
bash download.sh
```

# run
```
python3 index.py
```

# run swagger web server
```
export MODEL=./orca-mini-3b.ggmlv3.q8_0.bin
python3 -m llama_cpp.server
```

http://localhost:8000/docs