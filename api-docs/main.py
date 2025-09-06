import json
import os

def prefix_paths(paths, prefix):
	return {f"{prefix}{path}": value for path, value in paths.items()}

def merge_swagger_files():
	base_dir = os.path.dirname(os.path.abspath(__file__))
	files = [
		("./swagger/application-swagger.json", "/app-eda"),
		("./swagger/auth-swagger.json", "/auth"),
		("./swagger/customer-swagger.json", "/c"),
		("./swagger/lender-swagger.json", "/l"),
	]
	merged = {
		"swagger": "2.0",
		"info": {},
		"paths": {},
		"definitions": {},
	}
	for filename, prefix in files:
		path = os.path.join(base_dir, filename)
		with open(path, "r") as f:
			data = json.load(f)
		# Merge info (first file wins, others ignored)
		if not merged["info"] and "info" in data:
			merged["info"] = data["info"]
		# Merge paths with prefix
		if "paths" in data:
			merged["paths"].update(prefix_paths(data["paths"], prefix))
		# Merge definitions
		if "definitions" in data:
			merged["definitions"].update(data["definitions"])
	# Merge other top-level fields if needed
	output_path = os.path.join(base_dir, "swagger.json")
	with open(output_path, "w") as f:
		json.dump(merged, f, indent=2)
	print(f"Merged Swagger file saved to {output_path}")

if __name__ == "__main__":
	merge_swagger_files()
