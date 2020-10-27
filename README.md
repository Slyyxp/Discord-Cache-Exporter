## Overview
Discord-Cache-Exporter(discordce) is a package for exporting cached data files as .png 
 
This project was written with the intention of learning how to package a project.

### Installation
```console
pip install discordce
```

### Arguments
Argument  | Description  | Example
------------- | ------------- | -------------
-o, --output | Output directory | `Z:\Exported images`

### Usage Example
- Calling with no arguments will output to the working directory
```console
discordce
```

- Pass the --output/-o argument to output to specified folder.
```console
discordce --output "Z:\Exported images"
```