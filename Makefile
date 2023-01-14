#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER := python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Set up python interpreter environment
create_environment:
	$(PYTHON_INTERPRETER) -m venv .venv
	. .venv/bin/activate; pip install -U pip; pip install -r requirements.txt

## Make Dataset
data: create_environment
	. .venv/bin/activate; $(PYTHON_INTERPRETER) ./scripts/prepare_data.py