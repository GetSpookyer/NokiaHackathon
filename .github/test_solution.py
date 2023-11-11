import os
import sys
import time
import json
import subprocess

char_limit = 5000
cwd = str(sys.argv[1])
timeout = str(sys.argv[2])
print(json.dumps(sys.argv, sort_keys=True, indent=2))

start = time.time()
result = subprocess.run(
    [f'timeout {timeout} {sys.executable} main.py'],
    shell=True,
    capture_output=True,
    text=True,
    cwd=cwd
)
delta_time = time.time() - start

print(result.stdout)
print(result.stderr)
print(delta_time)

with open(os.path.join(cwd, 'result.json'), 'w') as f:
    json.dump({
        'output': result.stdout,
        'stderr': result.stderr,
        'returncode': result.returncode,
        'execution_time': delta_time,
    }, f, sort_keys=True, indent=2)
