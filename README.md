# Natural Language Processing(Python)

Detect sentence on basis of intent(specific words).

## Installation

Use the package manager [conda](https://www.anaconda.com/products/individual) to install.

```bash
conda create -n <yourenvname> python=3.7.4 anaconda
```

```bash
conda activate <yourenvname>
```

```bash
conda install --yes --file requirements.txt
```

## Usage

### To Execute api use postman collection in `postman-collection` folder.

To Train Model
```bash
python train.py
```

To Run Api
```bash
python app.py
```

To Test working
```bash
python test.py
```



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)