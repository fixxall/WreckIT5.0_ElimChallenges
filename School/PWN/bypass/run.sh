#!/bin/bash

socat tcp-l:9245,reuseaddr,fork exec:./bypass,stderr
