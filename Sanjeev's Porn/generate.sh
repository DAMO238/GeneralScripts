#!/bin/bash


while true
do
	URL="$(curl inspirobot.me/api?generate=true)"
	wget -O pic.jpg $URL
	display pic.jpg
done
