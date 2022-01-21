import datetime

from sfn_search import parse_executions, parse_desription, retrieve_matching_id

execution_list = {
    "executions": [
        {
            "executionArn": "arn:aws:states:us-east-1:111077548247:execution:prod-lakeVeranaCompaction:9c8e5609-f25d-4074-8de4-3def8657b281",
            "stateMachineArn": "arn:aws:states:us-east-1:111077548247:stateMachine:prod-lakeVeranaCompaction",
            "name": "9c8e5609-f25d-4074-8de4-3def8657b281",
            "status": "SUCCEEDED",
            "startDate": datetime.datetime(
                2022,
                1,
                21,
                6,
                17,
                8,
            ),
            "stopDate": datetime.datetime(
                2022,
                1,
                21,
                6,
                29,
                26,
                679000,
            ),
        },
        {
            "executionArn": "arn:aws:states:us-east-1:111077548247:execution:prod-lakeVeranaCompaction:ee074aca-ac3d-47b4-b4f4-f5c9a881b081",
            "stateMachineArn": "arn:aws:states:us-east-1:111077548247:stateMachine:prod-lakeVeranaCompaction",
            "name": "ee074aca-ac3d-47b4-b4f4-f5c9a881b081",
            "status": "SUCCEEDED",
            "startDate": datetime.datetime(
                2022,
                1,
                21,
                6,
                6,
                42,
                256000,
            ),
            "stopDate": datetime.datetime(
                2022,
                1,
                21,
                6,
                17,
                42,
                994000,
            ),
        },
    ],
    "nextToken": "AAAAKgAAAAIAAAAAAAAAAZbPDABbpDj/vrPXsphGDt7HSUYFgMeIAJ7TeD96EqBW2momV0BzEguVngKbgeU0m4b+28vZAUo8S8HjfgJa2g2K7Tyl88gS3MTiXFoZlj5wzPvWfLrNaBcKkU5dqaBBB/C15Nd2hdU9YrO5Dos6ETxjbkRjWL5ZuId+PKPVevwamKF7sIO2Ogcl04SN434niqdM8hhW3Om34RItuEMz8+SgmgGehNsIainRwYk0rNExH1rmiV1rOTTh1LYjWRwrV6V+O0Xx5465XbqNXEqyttCG04xUqfRNCRcU4hg196L1K1y/vczgkc+lTuWJWvk/Dxzavxq0gOSpIMDxqtidtTxrwuA8a9EkKkUKaphnFigkXML+IVn7JpFPbnBvTHHBxXD8K0+obGLG8TreocmKG10h+IAySEXNEHtnO/e2GH4svGQxh6Nh8bp2syYT87ZaGpSaSRGoW//LAdjItorZCRo=",
    "ResponseMetadata": {
        "RequestId": "91b9ce36-ad47-40c1-a1a0-e0c35a80a563",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "91b9ce36-ad47-40c1-a1a0-e0c35a80a563",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "1222",
        },
        "RetryAttempts": 0,
    },
}


def test_parse_executions():
    results = parse_executions(execution_list)
    expected = [
        (
            "9c8e5609-f25d-4074-8de4-3def8657b281",
            datetime.datetime(
                2022,
                1,
                21,
                6,
                17,
                8,
            ),
            "arn:aws:states:us-east-1:111077548247:execution:prod-lakeVeranaCompaction:9c8e5609-f25d-4074-8de4-3def8657b281",
        ),
        (
            "ee074aca-ac3d-47b4-b4f4-f5c9a881b081",
            datetime.datetime(
                2022,
                1,
                21,
                6,
                6,
                42,
                256000,
            ),
            "arn:aws:states:us-east-1:111077548247:execution:prod-lakeVeranaCompaction:ee074aca-ac3d-47b4-b4f4-f5c9a881b081",
        ),
    ]
    assert results == expected


execution_description = {
    "executionArn": "arn:aws:states:us-east-1:111077548247:execution:prod-lakeVeranaCompaction:ee074aca-ac3d-47b4-b4f4-f5c9a881b081",
    "stateMachineArn": "arn:aws:states:us-east-1:111077548247:stateMachine:prod-lakeVeranaCompaction",
    "name": "ee074aca-ac3d-47b4-b4f4-f5c9a881b081",
    "status": "SUCCEEDED",
    "startDate": datetime.datetime(
        2022,
        1,
        21,
        6,
        6,
        42,
        256000,
    ),
    "stopDate": datetime.datetime(
        2022,
        1,
        21,
        6,
        17,
        42,
        994000,
    ),
    "input": '"{\\"vh_deployment_id\\":\\"c58uq30dpdsci4h10n8g\\",\\"vh_pull_id\\":\\"c7l6h0d10000j41ufl2g\\",\\"s3_bucket\\":\\"vh-master-ue1-prod-data-lake\\",\\"s3_uri\\":\\"s3://vh-master-ue1-prod-data-lake/raw/ra_data/c58uq30dpdsci4h10n8g/c7l6h0d10000j41ufl2g\\"}"',
    "inputDetails": {"included": True},
    "output": '{"s3_bucket": "vh-master-ue1-prod-data-lake", "vh_deployment_id": "c58uq30dpdsci4h10n8g", "s3_uri": "s3://vh-master-ue1-prod-data-lake/raw/ra_data/c58uq30dpdsci4h10n8g/c7l6h0d10000j41ufl2g", "process_type": "historic", "body": "Glue Catalog Pass: True", "statusCode": 200}',
    "outputDetails": {"included": True},
    "ResponseMetadata": {
        "RequestId": "b152a924-91fc-4b43-8591-81a833378974",
        "HTTPStatusCode": 200,
        "HTTPHeaders": {
            "x-amzn-requestid": "b152a924-91fc-4b43-8591-81a833378974",
            "content-type": "application/x-amz-json-1.0",
            "content-length": "1161",
        },
        "RetryAttempts": 0,
    },
}


expected_parse_description = (
    "ee074aca-ac3d-47b4-b4f4-f5c9a881b081",
    datetime.datetime(
        2022,
        1,
        21,
        6,
        6,
        42,
        256000,
    ),
    '"{\\"vh_deployment_id\\":\\"c58uq30dpdsci4h10n8g\\",\\"vh_pull_id\\":\\"c7l6h0d10000j41ufl2g\\",\\"s3_bucket\\":\\"vh-master-ue1-prod-data-lake\\",\\"s3_uri\\":\\"s3://vh-master-ue1-prod-data-lake/raw/ra_data/c58uq30dpdsci4h10n8g/c7l6h0d10000j41ufl2g\\"}"',
)


def test_parse_description():
    results = parse_desription(execution_description)

    assert results == expected_parse_description


def test_retrieve_matching_id():
    not_match = (
        "not-ee074aca-ac3d-47b4-b4f4-f5c9a881b081",
        datetime.datetime(
            2022,
            1,
            21,
            6,
            6,
            42,
            256000,
        ),
        '"{\\"vh_deployment_id\\":\\"aaatttttt\\",\\"vh_pull_id\\":\\"c7l6h0d10000j41ufl2g\\",\\"s3_bucket\\":\\"vh-master-ue1-prod-data-lake\\",\\"s3_uri\\":\\"s3://vh-master-ue1-prod-data-lake/raw/ra_data/c58uq30dpdsci4h10n8g/c7l6h0d10000j41ufl2g\\"}"',
    )
    input_list = [not_match, expected_parse_description]
    results = retrieve_matching_id("c58uq30dpdsci4h10n8g", input_list)
    assert results == [expected_parse_description]
