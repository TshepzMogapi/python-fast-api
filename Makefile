run-main:
	uvicorn main:app --app-dir src  --host 0.0.0.0 --reload

run-notifier:
	uvicorn notifier:app --app-dir src  --host 0.0.0.0 --port 8088 --reload

install-dep:
	pip install -r requirements.txt