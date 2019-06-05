#!/bin/sh
docker_compose_zalenium.sh start
behave ./features/web --tags ~manual -D local=false -D testurl=$1 --junit --junit-directory reports
docker_compose_zalenium.sh stop
