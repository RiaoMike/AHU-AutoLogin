#!/bin/bash

state=$(curl -sIL www.google.com | grep HTTP | sed -n '$p' | awk '{print $2}')

if [ $state -eq 200 ]
then
  echo "Internet Access Successfully!"
fi
