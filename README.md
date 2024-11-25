# A little project to test a little lambda function

```bash
export AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION:-us-east-1}
export STACK_NAME=simple-lambda-python-stack
export TEMPLATE_FILE=simple_func.yaml
 
aws cloudformation create-stack --stack-name ${STACK_NAME} \
 --template-body file://$TEMPLATE_FILE --capabilities CAPABILITY_NAMED_IAM

aws cloudformation validate-template --template-body file://$TEMPLATE_FILE

aws cloudformation deploy --template-file $TEMPLATE_FILE --stack-name $STACK_NAME

aws cloudformation describe-stack-events --stack-name $STACK_NAME

aws cloudformation delete-stack --stack-name $STACK_NAME

aws cloudformation describe-stacks --stack-name $STACK_NAME
aws cloudformation describe-stacks --stack-name $STACK_NAME | jq '.Stacks[0].Outputs'

aws cloudformation describe-stacks --stack-name $STACK_NAME \
 --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" --output text

```

## Get events from logs

```bash
aws logs describe-log-streams --log-group-name "/aws/lambda/simple-lambda-python-stack-MyLambdaFunction-sd1JEU3Fhq7K" --order-by "LastEventTime" --descending 

arn:aws:lambda:us-east-1:642968566640:function:simple-lambda-python-stack-MyLambdaFunction-sd1JEU3Fhq7K

```

## Other 
```bash
# increase timeout 
aws lambda update-function-configuration \
    --function-name simple-lambda-python-stack-MyLambdaFunction-sd1JEU3Fhq7K \
    --timeout 10

```

## Change set

```bash
aws cloudformation create-change-set \
    --stack-name ${STACK_NAME} \
    --template-body file://$TEMPLATE_FILE \
    --parameters ParameterKey=InstanceType,ParameterValue=t2.large \
    --change-set-name ${STACK_NAME}-change-set-1
    
aws cloudformation describe-change-set --change-set-name $STACK_NAME

aws cloudformation execute-change-set --change-set-name $STACK_NAME
  
```

