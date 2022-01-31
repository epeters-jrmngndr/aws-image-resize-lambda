# aws-lambda-example

## Invocation Example

aws lambda invoke --function-name manualActions --log-type Tail --payload '{ "action": "increment", "number": 50 }' /dev/stdout
