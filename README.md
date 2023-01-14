# Cats vs dogs

Consume Keras model in C++ application.

Implements solution for [Kaggle Dogs vs. Cats competition](https://www.kaggle.com/c/dogs-vs-cats).

## Requirements

This project uses Keras for training model and frugally-deep and OpenCV for model consumer. Additionally, Python3, Make and CMake are required.

Python requirements are handled by the Make commands and the virtual environment. To install frugally-deep dependencies, follow the installation instructions on the [repository page](https://github.com/Dobiasd/frugally-deep).

To download the dataset, you need to enable the [Kaggle API](https://www.kaggle.com/docs/api).

Tested on Ubuntu 20.04.

## Usage

All build steps are handled by Make commands. You can run them manually.

**Note:** Installed Tensorflow requires a CUDA enabled GPU. You can run data preprocessing and model training steps e.g. in Google Colab. Copy the content of the necessary scripts to the cloud. Next, download the model and place it in the `models` directory inside the project directory.

### Creating environment

This step assumes the `python3-venv` and `python3-pip` (on Ubuntu) packages are installed. Just run:

```
make environment
```

Or manually:

```
python3 -m venv .venv
. .venv/bin/activate
pip install -U pip
pip install -r requirements.txt
```

### Data preprocessing

```
make data
```

Or manually:

```
python3 ./scripts/prepare_data.py
```

### Model training

```
make model
```

Or manually:

```
python3 ./train/train_model.py
```

### Model converting

```
make convert
```

Or manually:

```
python3 ./scripts/convert_model.py ./models/CatVsDog.h5 ./models/CatVsDog.json
```

### Build model consumer

```
make consumer
```

Or manually:

```
mkdir -p build && cd build
cmake ..
make
```

### Run consumer

```
./build/cats-vs-dogs /path/to/CatVSDog.json /path/to/image
```

Values ​​greater than 0.5 mean that predicted class is dog and lesser values - cat.

## Acknowledgements

Project structure inspired by [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/).

Model architecture created by [dandwvs](https://www.kaggle.com/code/dandwvs/dogs-vs-cats-cnn).

[frugally-deep](https://github.com/Dobiasd/frugally-deep) and [FunctionalPlus](https://github.com/Dobiasd/FunctionalPlus) libraries developed by [Tobias Hermann](https://github.com/Dobiasd).

[json](https://github.com/nlohmann/json) library by [Niels Lohmann](https://github.com/nlohmann).

C++ linear algebra library [Eigen3](https://gitlab.com/libeigen/eigen).