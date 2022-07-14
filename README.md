# ciphers-py
Python CLI app for text transformation with the following alphanumeric ciphers:
- ROT13
- Caesar
- Vigenere

## Demo
```
$ ./bin/ciphers rot13 -m "Curiouser and curiouser!"         
Running ROT13 cipher on message:                                                                        
Curiouser and curiouser!                                                                                
Ciphertext is:                                                                                          
Phevbhfre naq phevbhfre!                                                                                

$ ./bin/ciphers caesar -m "Curiouser and curiouser!" -k 5   
Running Caesar cipher with shift value 5 on message:                                                    
Curiouser and curiouser!                                                                                
Ciphertext is:                                                                                          
Hzwntzxjw fsi hzwntzxjw!

$ ./bin/ciphers vigenere -m "Curiouser and curiouser!" -k Alice                                                                       
Running Vigenere cipher with keyword Alice on message:                                   
Curiouser and curiouser!                                                                 
Ciphertext is:                                                                           
Cfzksudmt eno kwvizcuir!                                                                                                          
```

## Usage
A Debian 11 Docker container is used to build, format, test, and run the Ciphers tool.

### System Requirements
- Unix-based system (Linux, MacOS, or WSL on Windows)
- Docker Engine
- `make`

List of available `make` targets:
```
$ make help
image   Build Docker development image
shell   Run shell into Docker development container
format  Run Black Python code formatter
build   Build ciphers-py executable
test    Run unit tests
clean   Remove all build content
help    List all available make target
```

### Bulid & Run Docker Image
First build the project's Docker image:
```
make image
```

Then run a container with an interactive Bash shell. The project directory will be mounted as the current working directory:
```
make shell
```

### Build & Run Ciphers Tool
Run PyInstaller to build the project into a single-file executable, available in `bin/`:
```
make build
```

See full help text for requirements of each cipher:
```
$ ./bin/ciphers -h
usage: main parser [-h] {rot13,caesar,vigenere} ...
                                                                    
positional arguments:                                               
  {rot13,caesar,vigenere}                                           
                        ciphers parsers                             
    rot13               rot13 help                                  
    caesar              caesar help                                 
    vigenere            vigenere help                               
                                                                    
options:                                                            
  -h, --help            show this help message and exit             

```

## Development
The Docker container can also be used to format and test code changes.

### Format
Run Black code formatter on Python files:
```
make format
```

### Test
Run unit tests, written in Pytest:
```
make test
```
