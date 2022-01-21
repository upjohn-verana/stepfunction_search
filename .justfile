default:
    @just --list

tests:
    PYTHONPATH=src poetry run pytest ./tests
