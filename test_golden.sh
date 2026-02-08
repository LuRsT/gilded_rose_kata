#!/bin/bash

diff golden.txt <(uv run python produce_golden.py 2>&1)
