import json
import boto3

def lambda_handler(event, context):
    body = None
    status_code = 200
    headers = {
        "Content-Type": "application/json"
    }

    dynamodb = boto3.client("dynamodb")

    try:
        if event["routeKey"] == "DELETE /items/{id}":
            dynamodb.delete_item(
                TableName="http-crud-tutorial-items",
                Key={
                    "id": {"S": event["pathParameters"]["id"]}
                }
            )
            body = f"Deleted item {event['pathParameters']['id']}"
        elif event["routeKey"] == "GET /items/{id}":
            response = dynamodb.get_item(
                TableName="http-crud-tutorial-items",
                Key={
                    "id": {"S": event["pathParameters"]["id"]}
                }
            )
            body = response["Item"]
        elif event["routeKey"] == "GET /items":
            response = dynamodb.scan(
                TableName="http-crud-tutorial-items"
            )
            body = response["Items"]
        elif event["routeKey"] == "PUT /items":
            request_json = json.loads(event["body"])
            dynamodb.put_item(
                TableName="http-crud-tutorial-items",
                Item={
                    "id": {"S": request_json["id"]},
                    "price": {"N": str(request_json["price"])},
                    "name": {"S": request_json["name"]}
                }
            )
            body = f"Put item {request_json['id']}"
        else:
            raise ValueError(f"Unsupported route: {event['routeKey']}")
    except Exception as err:
        status_code = 400
        body = str(err)
    finally:
        body = json.dumps(body)

    return {
        "statusCode": status_code,
        "body": body,
        "headers": headers
    }
