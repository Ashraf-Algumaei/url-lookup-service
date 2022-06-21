local-deploy:
	docker build . --target builder -t urllookupservice 
	docker run -p 3002:80 -t -i --env-file .env urllookupservice