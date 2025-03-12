import os

project_name = 'project_structure'

print('Create project structure...')

dirs = ["data","models","src"]
scripts = ['data_ingestion.py', 'prepocessing.py', 'feature_engineering.py', 'train.py', 'evaluate.py', 'inference.py']
other_files = ['pipeline.py', 'requirements.txt']
new_dirs = ['1']
os.makedirs(project_name, exist_ok=True)
file_path = None

for x in dirs:
    file_path = os.path.join(project_name, str(x))
    print(f'Create directory: {file_path}')
    os.makedirs(file_path, exist_ok=True)

for y in scripts:
    new_path = os.path.join(file_path, str(y))
    print(f'Create script: {new_path}')
    with open(new_path, "w") as file: None

for z in other_files:
    nw = os.path.join(project_name, str(z))
    print(f'Create script: {nw}')
    with open(nw, "w") as file: None

print("Структура проекта и Python-скрипты созданы!")
