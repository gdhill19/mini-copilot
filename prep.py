import ast
import random
from pathlib import Path

all_files = list(Path("data/repos").rglob("*.py"))
print("Python files found:", len(all_files))

good_files = []

for file in all_files:
    try:
        code = file.read_text(encoding="utf-8")
    except:
        continue

    if len(code.splitlines()) < 10:
        continue

    try:
        ast.parse(code)
    except:
        continue

    good_files.append(str(file))

print("Good files kept:", len(good_files))


random.seed(42)            
random.shuffle(good_files)

split_point = int(len(good_files) * 0.7)
train_files = good_files[:split_point]    
test_files = good_files[split_point:]     

print("Training files:", len(train_files))
print("Testing files:", len(test_files))


Path("data/splits").mkdir(exist_ok=True)

with open("data/splits/train.txt", "w") as f:
    f.write("\n".join(train_files))

with open("data/splits/test.txt", "w") as f:
    f.write("\n".join(test_files))

print("Saved train.txt and test.txt")