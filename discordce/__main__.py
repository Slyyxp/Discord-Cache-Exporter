import argparse


def get_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('-o', '--output', nargs="*", help="URL.", required=True)
	return parser.parse_args()


def main():
	args = get_args()


if __name__ == '__main__':
	main()
