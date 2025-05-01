include .env

start: setup-docker-compose  create-dynamodb-table list-tables

setup-docker-compose:
	docker-compose up -d --build

create-dynamodb-table:
	docker-compose exec localstack awslocal dynamodb create-table \
    --table-name ${TABLE_DYNAMO} \
    --key-schema AttributeName=id,KeyType=HASH \
    --attribute-definitions AttributeName=id,AttributeType=S \
    --billing-mode PAY_PER_REQUEST \
    --region ${AWS_REGION}

list-tables:
	docker-compose exec localstack awslocal dynamodb list-tables
 
stop:
	docker-compose down