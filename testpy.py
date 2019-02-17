import json
import sys


tmp1 = []
tmp = {"gay":"gay"};
tmp1.append(tmp)
x = sys.stdin.readline()
sys.stderr.write(x)

print(json.dumps(tmp1))