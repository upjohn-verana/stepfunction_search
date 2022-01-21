"""
usage:
    `python sfn_search.py <deployment_id>`

    this assumes that you have boto3 installed in your virtualenv

Note:
This works on just successful sfn executions. You can change it to include other states
"""
import re
import sys
from typing import Dict, List, Tuple

import boto3

sfn_arn = "arn:aws:states:us-east-1:111077548247:stateMachine:prod-lakeVeranaCompaction"


def get_client():
    sfn = boto3.client("stepfunctions")
    return sfn


def parse_executions(executions: Dict) -> List[Tuple]:
    list_of_executions = executions["executions"]
    execution_parts = [(i["name"], i["startDate"], i["executionArn"]) for i in list_of_executions]
    return execution_parts


def get_executions(max_result: int = 100) -> Dict:
    sfn = get_client()
    response = sfn.list_executions(
        stateMachineArn=sfn_arn,
        statusFilter="SUCCEEDED",
        maxResults=max_result,
    )
    return response


def parse_desription(execution_description: Dict) -> Tuple:
    description = (execution_description["name"], execution_description["startDate"], execution_description["input"])
    return description


def get_definition(execution_id: str) -> Dict:
    sfn = get_client()
    response = sfn.describe_execution(executionArn=execution_id)
    return response


def retrieve_matching_id(deployment_id: str, execution_input: List[Tuple]) -> List:
    def get_deployment_id_from_string(input_string: str) -> str:
        match_pattern = r'("vh_dep.*?:.*?")(.*?)\\'
        found = re.search(
            match_pattern,
            input_string,
        )
        match = ""
        if len(found.groups()) > 0:
            match = found.groups()[1]
        return match

    matching = [i for i in execution_input if deployment_id in get_deployment_id_from_string(i[2])]
    return matching


def output_result(matching_results: List[Tuple]) -> str:
    printable = "\n".join([f"sfn execution id: {i[0]}, started: {i[1].isoformat()}" for i in matching_results])
    return printable


def main(deployment_id):
    last_executions = get_executions(10)
    executions_arn = parse_executions(last_executions)
    definitions_raw = [get_definition(i[2]) for i in executions_arn]
    definitions_parsed = [parse_desription(i) for i in definitions_raw]
    matching_sfn = retrieve_matching_id(deployment_id, definitions_parsed)

    printing = output_result(matching_sfn)

    return printing


if __name__ == "__main__":
    if len(sys.argv) > 1:
        deployment_id = sys.argv[1]
    else:
        print("Need deployment id to be passed as an argument")
        raise Exception("No deployment passed")

    print(f"\nResults for deployment id {deployment_id}\n")

    results = main(deployment_id)
    printable_results = results if results != "" else "No results"
    print(printable_results)
