#!/bin/bash

echo "Current Space of /var/log :" > current-space.txt
du -sh /var/log >> current-space.txt
echo "Current Free/Used Space of system:" >> current-space.txt
df -h >> current-space.txt
