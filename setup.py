from setuptools import setup

setup(
	name="discordce",
	version="0.1.0",
	packages=['discordce'],
	entry_points={
		'console_scripts': [
			'discordce = discordce.__main__:main'
		]
	})
