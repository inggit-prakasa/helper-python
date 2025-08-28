import json

pijar_auth = {}

try:
    with open('json-comparator/pijar-auth.json', 'r') as f:
        pijar_auth = json.load(f)
except FileNotFoundError:
    print("File pijar-auth.json tidak ditemukan.")

pijar_auth_paths = []
print("\n--- Pijar Auth Paths ---\n")

for path, info in pijar_auth.get('paths', {}).items():
    for method, details in info.items():
        itemPath += 1
        # print(f"{method.upper()} {path}")
        pijar_auth_paths.append(f"{method.upper()} {path}")


print("\n--- Krakend Endpoints ---\n")

krakend_auth_paths = []

# Get krakend json
krakend = {}

try:
    with open('json-comparator/krakend.json', 'r') as f:
        krakend = json.load(f)
except FileNotFoundError:
    print("File krakend.json tidak ditemukan.")

totalItem = 0
for info in krakend.get('endpoints', []):
    if info.get('endpoint', '').startswith('/auth/'):
        # print(f"{info.get('method', '')} {info.get('endpoint').replace('/auth', '')}")
        krakend_auth_paths.append(f"{info.get('method', '')} {info.get('endpoint').replace('/auth', '')}")
        totalItem += 1

print(f"Total endpoints found: {totalItem}")

# Compare both
print("\n--- Comparison Results ---\n")
only_in_pijar_auth = set(pijar_auth_paths) - set(krakend_auth_paths)
only_in_krakend = set(krakend_auth_paths) - set(pijar_auth_paths)

if only_in_pijar_auth:
    print("Paths only in pijar-auth.json:")
    for path in only_in_pijar_auth:
        print(path)
else:
    print("No unique paths in pijar-auth.json.")

if only_in_krakend:
    print("\nEndpoints only in krakend.json:")
    for path in only_in_krakend:
        print(path)
else:
    print("No unique endpoints in krakend.json.")