.PHONY: build
build:
	make -C locust build

.PHONY: deploy
deploy:
	kubectl apply -f manifests/hpa -n load-testing-hpa
	kubectl apply -f manifests/hybrid-scaler -n load-testing-hybrid-scaler

.PHONY: undeploy
undeploy:
	kubectl delete -f manifests/hpa -n load-testing-hpa
	kubectl delete -f manifests/hybrid-scaler -n load-testing-hybrid-scaler
