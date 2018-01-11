import os
import sys
import tempfile

if len(sys.argv) <= 1:
    print('Usage: python main.py <zip file>')
    exit(-1)

decomp_path = 'C:\\Progra~1\\7-Zip\\7z.exe'
if not os.path.exists(decomp_path):
    print('Install 64-bit 7-zip before continuing')
    exit(-1)

zip_file_path = sys.argv[1]

temp_dir = tempfile.mkdtemp()
print(temp_dir)
decompress_cmd = '{} e {} -o{}'.format(decomp_path, zip_file_path, temp_dir)
print(decompress_cmd)
os.system(decompress_cmd)


for f in os.listdir(temp_dir):
    if '.log' in f:
        log_file = open(os.path.join(temp_dir, f), 'r')
        for line in log_file.readlines():
            s = line.split()
            if len(s) > 3 and s[2] == 'E':
                print(line)
        log_file.close()
