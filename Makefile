#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
PYTHON_INTERPRETER := python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Set up python interpreter environment
environment:
	$(PYTHON_INTERPRETER) -m venv .venv
	. .venv/bin/activate; pip install -U pip; pip install -r requirements.txt

## Make Dataset
data:
	. .venv/bin/activate; $(PYTHON_INTERPRETER) ./scripts/prepare_data.py

## Make Model
model:
	. .venv/bin/activate; $(PYTHON_INTERPRETER) ./train/train_model.py

## Convert a Keras model to frugally-deep format
convert:
	. .venv/bin/activate; $(PYTHON_INTERPRETER) ./scripts/convert_model.py \
	$(PROJECT_DIR)/models/CatVsDog.h5 $(PROJECT_DIR)/models/CatVsDog.json

## Make Consumer
consumer:
	mkdir -p build && cd build && cmake .. && make