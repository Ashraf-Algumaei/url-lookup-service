lint:
	flake8 app --ignore E501,W503 

test:
	docker build --target tests \
	--build-arg COSMOS_DB_MASTER_KEY=$(COSMOS_DB_MASTER_KEY) .

local-deploy: lint test
	docker build . --target builder -t urllookupservice 
	docker run -p 3002:80 -t -i --env-file .env urllookupservice