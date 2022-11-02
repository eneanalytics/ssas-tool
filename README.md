# ssas-tool
Clean your SSAS model file from all uppercase column names that often is the
  result of reading data from a database such as Snowflake. Input the path to
  the Model.bim file in the MODEL_FILE_PATH argument and then the path to the
  output file in the MODEL_FILE_OUTPUT_PATH argument.

  I.e. python main.py Model.bim Model_clean.bim


## Installation

### Clone the repository


### With pip
    pip install -r requirements.txt

### With poetry
    poetry install

## Usage
```
❯ python clean_bim.py --help
Usage: clean_bim.py [OPTIONS] MODEL_FILE_PATH MODEL_FILE_OUTPUT_PATH

  Clean your SSAS model file from all uppercase column names that often is the
  result of reading data from a database such as Snowflake. Input the path to
  the Model.bim file in the MODEL_FILE_PATH argument and then the path to the
  output file in the MODEL_FILE_OUTPUT_PATH argument. I.e.

  python clean_bim.py Model.bim Model_clean.bim

Arguments:
  MODEL_FILE_PATH         The full path to the Model.bim file  [required]
  MODEL_FILE_OUTPUT_PATH  The full path to where you want to store the
                          processed file  [required]

Options:
  --rename-tables / --no-rename-tables
                                  If you want to rename tables. It may mean
                                  that you have to reprocess them in SSAS
                                  [default: no-rename-tables]
  --install-completion [bash|zsh|fish|powershell|pwsh]
                                  Install completion for the specified shell.
  --show-completion [bash|zsh|fish|powershell|pwsh]
                                  Show completion for the specified shell, to
                                  copy it or customize the installation.
  --help                          Show this message and exit.


```