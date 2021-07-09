import sys
import hashlib

DEFAULT_ALGORYTHM = 'md5'

if len(sys.argv) > 1:
    algorythm = sys.argv[1]
else:
    algorythm = input('which algorythm: ') or DEFAULT_ALGORYTHM

if algorythm not in hashlib.algorithms_guaranteed:
    print(f"sorry, algorythm {algorythm} is not available")
    print(f"available algorythms: {hashlib.algorithms_guaranteed}")

print(f"selected algorythm: {algorythm}")
