import os, subprocess

my_env = os.environ.copy()
my_env["MODEL_ID"] = 'TabbyML/StarCoder-3B'

p = subprocess.Popen(["modal", "run", "./modal/predict.py","--language", 'python'], env=my_env)
p.wait()

