# A little project to test a little lambda function

```bash
export AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION:-us-east-1}
export STACK_NAME=simple-lambda-python-stack
export TEMPLATE_FILE=simple_func.yaml
 
aws cloudformation create-stack --stack-name ${STACK_NAME} \
 --template-body file://$TEMPLATE_FILE --capabilities CAPABILITY_NAMED_IAM

aws cloudformation deploy --template-file file://$TEMPLATE_FILE --stack-name $STACK_NAME

aws cloudformation describe-stack-events --stack-name $STACK_NAME

#aws cloudformation delete-stack --stack-name $STACK_NAME

aws cloudformation describe-stacks --stack-name $STACK_NAME
aws cloudformation describe-stacks --stack-name $STACK_NAME | jq '.Stacks[0].Outputs'

aws cloudformation describe-stacks --stack-name $STACK_NAME \
 --query "Stacks[0].Outputs[?OutputKey=='ApiUrl'].OutputValue" --output text

```