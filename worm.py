# ⚠️ DISCLAIMER:
# This project is for educational and ethical cybersecurity research purposes only.
# It simulates the behavior of a computer worm in a controlled environment.
# The author does NOT condone or promote any form of unauthorized access, data breach, or malicious activity.
# DO NOT deploy or distribute this code in real-world environments.
# Misuse of this project may be illegal and subject to criminal charges.
# By using this code, you agree to take full responsibility and comply with all applicable laws and ethical guidelines.

import shutil
import os
import sys

if len(sys.argv) == 2:
    for num in range(0, int(sys.argv[1])):
        shutil.copy(sys.argv[0], sys.argv[0] + f'{num}.py')
else:
    print('Envia 2dos parámetros')