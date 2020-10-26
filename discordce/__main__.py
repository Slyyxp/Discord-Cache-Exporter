import argparse
import os


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--output', nargs="*", help="URL.", required=False)
	return parser.parse_args()

# Verify that the cache folder exists.
def verify_cache():
	path = os.path.join(os.getenv("APPDATA"), "discord", "Cache")
	if os.path.exists(path):
		return path
	else:
		return None

def main():
	args = get_args()
	cache = verify_cache()

if __name__ == '__main__':
	main()
