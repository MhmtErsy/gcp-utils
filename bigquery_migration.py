import json
import subprocess

source_project_id = "crdr-lightnift"
target_project_id = "icat-crdr"
dataset_id = "crdr"

tables_json = subprocess.check_output(["bq", "ls", 
                                       "--format=prettyjson",
                                       f"--project_id={source_project_id}", dataset_id])
tables = json.loads(tables_json)

for table in tables:
    table_id = table["tableReference"]["tableId"]
    if table_id != 'cumulative_balance_copy' and table_id != 'contracts':
        print(f"bq cp {source_project_id}:{dataset_id}.{table_id} {target_project_id}:{dataset_id}.{table_id}")
        result = subprocess.run(["bq", "cp", f"{source_project_id}:{dataset_id}.{table_id}", 
                                               f"{target_project_id}:{dataset_id}.{table_id}"],  stdout=subprocess.PIPE)
        print(result.stdout)