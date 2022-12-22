import os
import sys

if __name__ == '__main__':
    with open('random_wallpaper.bat', 'w') as f:
        f.write('pushd "%~dp0" \n')
        python_path = sys.executable
        script_path = os.path.abspath('random_wallpaper.py')
        f.write(f'"{python_path}" "{script_path}"\n')
        f.close()