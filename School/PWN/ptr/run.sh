#!/bin/bash

socat tcp-l:10201,reuseaddr,fork exec:./introtoptr,stderr
