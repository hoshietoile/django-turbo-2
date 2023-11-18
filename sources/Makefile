dev-backend:
	make -C backend/ dev

dev-frontend:
	make -C frontend/ dev

dev-all:
	make -j dev-backend dev-frontend

generate-types:
	make -C backend/ generate-types && make -C frontend/ generate-types