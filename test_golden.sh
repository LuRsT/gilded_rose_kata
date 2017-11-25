#!/bin/bash
diff golden.txt <(python produce_golden.py 2>&1)
