import os
import sys
import json
import requests

server_url = str(sys.argv[1])
matrix_value = json.loads(sys.argv[2])
github_repository = str(sys.argv[3])
github_run_id = str(sys.argv[4])
github_sha = str(sys.argv[5])
print(json.dumps(sys.argv, sort_keys=True, indent=2))


def getResultJson(file_name):
    if os.path.isfile(file_name):
        with open(file_name) as f:
            return json.load(f)
    return {}


body = {"meta": {
    'repository': github_repository,
    'run_id': github_run_id,
    'sha': github_sha
}, "tasks": {}}

for item in matrix_value['include']:
    dirname = item['folder']

    body["tasks"][dirname] = getResultJson(
        os.path.join(dirname, 'result.json')
    )

print(json.dumps(body, sort_keys=True, indent=2))
res = requests.post(os.path.join(
    server_url, 'github-bot-finished/'), json=body)
if res.status_code >= 400:
    exception_msg = res.text
    try:
        exception_msg = json.dumps(res.json(), sort_keys=True, indent=2)
    except:
        pass

    raise Exception(exception_msg + '\nServer didn\'t like this :(')
