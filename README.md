# cw-nnrec

[![Build](https://github.com/andinoriel/cw-nnrec/actions/workflows/build.yml/badge.svg)](https://github.com/andinoriel/cw-nnrec/actions/workflows/build.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Just a few variants of using neural networks with pretrained models.

## Usage

1. Clone this project and then cd to the project folder;

2. Download trained neural modals:
```
$ python configure.py
```

3. Install the application:
```
$ pip install .
```

4. Run installed application with help message:
```
$ cw-nnrec --help
```

## Testing

Run project tests:
```
$ pytest --verbose
```

## Screenshots

<details>
  <summary>Expand</summary>

  <p align="center">
    <img src="screenshots/help.png" width="670"/>
    <img src="screenshots/equal.png" width="670"/>
    <img src="screenshots/not-equal.png" width="670"/>
  </p>
</details>

## License

This project is licensed under the [MIT License](LICENSE).

## Credits

* [Dlib](http://dlib.net/) - ML library
* [alesanfra](https://github.com/alesanfra/dlib-wheels) - for binary Dlib distribution

