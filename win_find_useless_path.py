import os
for path in os.getenv('Path').split(';'):
    if not os.path.exists(path):
        print(path)
    else:
        for (root, dirs, files) in os.walk(path):
            if len(files) > 0:
                break
        else:
            print(path)
