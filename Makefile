image:
	sudo docker build -t sdll .
enter: clean
	sudo docker run -it -p 8000:8000 \
									-e DISPLAY=$DISPLAY \
									-v /var/run/dbus/system_bus_socket:/var/run/dbus/system_bus_socket \
									-v /tmp/.X11-unix:/tmp/.X11-unix \
									-v /etc/localtime:/etc/localtime:ro \
									-v /home/sdll/dev/sdll:/home/sdll \
									-w /home/sdll --name=sdll \
									sdll
create: clean
	sudo docker run -d -t -p 8000:8000 \
									-v /home/sdll/dev/sdll:/home/sdll \
									-w /home/sdll --name=sdll \
									sdll
build: create
	sudo docker exec -d sdll stack clean --allow-different-user && echo "Cleaned up sdll."
	sudo docker exec -d sdll stack build --allow-different-user && echo "Built sdll."

rebuild-site: build
	sudo docker exec -it -d sdll stack exec --allow-different-user site rebuild

watch-site: build
	sudo docker exec -it -d sdll stack exec --allow-different-user site watch

clean:
	sudo docker stop sdll && sudo docker rm sdll || echo "No sdll container found."
