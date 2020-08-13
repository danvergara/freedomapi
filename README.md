# Freedom API

> REST API project written in python, using FastAPI as web framework, that proccessed data from the Heritage Foudation

Installation:

This projects runs in linux containers, so, there is all you need to run it
with docker.

You can run the project and other tasks using the Makefile included in the
project

```sh
$ make help

Usage:
  help            Prints this help message
  down            brings down the containers and volumes
  up              brings the contai back up
  test            runs all the tests in the app
  silent-test     runs all tests in the app disabling warnings
  test-ping       runs all tests that have ping in their name
  test-summary    runs all tests that have summary in their name
  test-read       runs all the test that have read in their name
  test-cov        runs the tests with coverage
  test-html-cov   generates a html report on testing coverage
  unit-test       run the unit test in parallel
  flake           runs flake8
  black-check     runs the black checker
  black-diff      shows the possible result of the black formatter
  black           runs the black formatter
  isort-check     check the order of the imports
  isort-diff      shows the differences after apply the changes
  isort            quickly sort all our imports alphabetically and automatically separate them into sections
```
