# Stepfunction Search

This script is to built to search the prod lake compaction stepfunction.  It searches for a given
deployment_id in the `execution_input` and returns the execution number and date.

It only searches the last 100 sfn executions and only successful executions.


The code can be changed to search more executions and also more states.

## Usage

There is a just "brew" (similar to make targets).  You use it after `brew install just`.

`just run <deployment_id>`

or `poetry run python src/sfn_search.py <deployment_id>`
