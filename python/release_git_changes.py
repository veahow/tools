# coding=utf-8
import os
import shutil
import datetime

docname = "./readme.txt"
list_command = "tree"
git_command = "git show --pretty=\"format:\" --name-only"
release_base_dirname = 'SourceRelease'
rel_git_paths = [
    'kernel',
    'sdk',
    'project'
]

def release_git_change(release_base_path, git_path, rel_git_path):
    os.chdir(git_path)
    print("%s git path releasing..." % os.getcwd())
    changes = os.popen(git_command)
    while True:
        change = changes.readline()
        if not change:
            break
        release_dir = os.path.join(rel_git_path, change.strip()).rsplit(os.sep, 1)[0] + os.sep
        release_path = os.path.join(release_base_path, release_dir)
        release_change = os.path.join(git_path, change.strip())
        try:
            shutil.copy2(release_change, release_path)
        except (FileNotFoundError, IsADirectoryError):
            os.makedirs(release_path, exist_ok=True)
            shutil.copy2(release_change, release_path)

def main():
    script_base_path = os.getcwd()
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime('%Y%m%d%H%M%S')
    release_dirname = formatted_time + '_' + release_base_dirname
    release_base_path = os.path.join(script_base_path, release_dirname)
    if os.path.exists(release_base_path) == True:
        shutil.rmtree(release_base_path)
    for index in range(0, len(rel_git_paths)):
        rel_git_path = rel_git_paths[index]
        git_path = os.path.join(script_base_path, rel_git_path)
        if os.path.exists(git_path) == True:
            release_git_change(release_base_path, git_path, rel_git_path)
        else:
            print('%s do not exits!' % git_path)
    os.chdir(release_base_path)
    lists = os.popen(list_command)
    context = lists.read()
    print(context)
    with open(docname, "w") as file:
        file.write(context)

if __name__ == '__main__':
    main()
