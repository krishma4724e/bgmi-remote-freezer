#!/bin/bash
PORT=$1
DURATION=$2
sudo iptables -A INPUT -p tcp --dport $PORT -j DROP
sleep $DURATION
sudo iptables -D INPUT -p tcp --dport $PORT -j DROP
