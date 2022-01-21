default:
    @just --list

tests:
    PYTHONPATH=src poetry run pytest ./tests

run:
    poetry run python src/sfn_search.py
