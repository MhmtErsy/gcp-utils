import json
import subprocess
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--source_project_id")
parser.add_argument("--source_dataset_id")
parser.add_argument("--target_project_id")
parser.add_argument("--target_dataset_id")


args = parser.parse_args()


source_project_id = args.source_project_id
target_project_id = args.target_project_id
source_dataset_id = args.source_dataset_id
target_dataset_id = args.target_dataset_id

print(source_dataset_id)

tables_json = subprocess.check_output(["bq", "ls", 
                                       "--format=prettyjson",
                                       f"--project_id={source_project_id}", source_dataset_id])
tables = json.loads(tables_json)

for table in tables:
    table_id = table["tableReference"]["tableId"]
    print(["bq", "cp", "--force", f"{source_project_id}:{source_dataset_id}.{table_id}", 
                                         f"{target_project_id}:{target_dataset_id}.{table_id}"])
    result = subprocess.run(["bq", "cp", "--force", f"{source_project_id}:{source_dataset_id}.{table_id}", 
                                         f"{target_project_id}:{target_dataset_id}.{table_id}"], stdout=subprocess.PIPE)
    print(result.stdout)