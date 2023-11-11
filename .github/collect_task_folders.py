import os
import sys
import json
import requests

server_url = str(sys.argv[1])
github_repository = str(sys.argv[2])
github_run_id = str(sys.argv[3])
print(json.dumps(sys.argv, sort_keys=True, indent=2))

include_value = []
excluded_folders = ['.git', '.github']

body = {"meta": {
    'repository': github_repository,
    'run_id': github_run_id
}}

print(json.dumps(body, sort_keys=True, indent=2))
requests.post(os.path.join(
    server_url, 'github-bot-started/'), json=body)

for item in os.listdir(os.getcwd()):
    if os.path.isdir(item) and item not in excluded_folders:
        include_value.append({
            "folder": item
        })

matrix_value = {"include": include_value}

output = f'matrix={json.dumps(matrix_value)}'
output_path = os.getenv('GITHUB_OUTPUT')

print(output)

if output_path is not None:
    with open(output_path, 'w') as f:
        f.write(output)
