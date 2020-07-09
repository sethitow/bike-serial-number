.PHONY: build rollout

build:
	docker build frontend
	docker build backend

rollout:
	kubectl rollout restart deployment serialnumber-frontend -n=serialnumber
	kubectl rollout restart deployment serialnumber-backend -n=serialnumber