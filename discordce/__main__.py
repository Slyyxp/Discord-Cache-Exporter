import argparse
import os
from shutil import copy

from discordce import exceptions


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--output', nargs="*", help="URL.", required=False)
	return parser.parse_args()


def verify_cache():
	path = os.path.join(os.getenv("APPDATA"), "discord", "Cache")
	if os.path.exists(path):
		return path
	else:
		raise exceptions.CacheNotFound("Cache was not found in the expected location: {}".format(path))


def export(cache_folder, output_folder):
	if output_folder is None:
		export_path = os.getcwd()
	else:
		export_path = output_folder[0]
	print(export_path)
	for file in os.listdir(cache_folder):
		if file.startswith("data"):
			pass
		elif file.startswith("index"):
			pass
		else:
			copy(os.path.join(cache_folder, file), os.path.join(export_path, "{}.png".format(file)))


def main():
	args = get_args()
	cache_folder = verify_cache()
	export(cache_folder, args.output)


if __name__ == '__main__':
	main()
