# ssas-tool
Clean your SSAS model file from all uppercase column names that often is the
  result of reading data from a database such as Snowflake. Input the path to
  the Model.bim file in the MODEL_FILE_PATH argument and then the path to the
  output file in the MODEL_FILE_OUTPUT_PATH argument.

  I.e. python main.py Model.bim Model_clean.bim


## Installation

### With pip
    pip install -r requirements.txt

### With poetry
    poetry install

## Usage
```
❯ python main.py --help
Usage: main.py [OPTIONS] MODEL_FILE_PATH MODEL_FILE_OUTPUT_PATH

  Clean your SSAS model file from all uppercase column names that often is the
  result of reading data from a database such as Snowflake. Input the path to
  the Model.bim file in the MODEL_FILE_PATH argument and then the path to the
  output file in the MODEL_FILE_OUTPUT_PATH argument.

  I.e. python main.py Model.bim Model_clean.bim

Arguments:
  MODEL_FILE_PATH         [required]
  MODEL_FILE_OUTPUT_PATH  [required]

Options:
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.

```