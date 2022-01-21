default:
    @just --list

pre-commit:
    pre-commit install

tests:
    PYTHONPATH=src poetry run pytest ./tests

run deployment_id:
    poetry run python src/sfn_search.py {{deployment_id}}
