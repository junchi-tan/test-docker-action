import os


def run():
    with open(os.environ['GITHUB_OUTPUT'], 'a') as gh_output:
        print(f'dirlist={os.listdir()}', file=gh_output)
        print(f'work_dir={os.getcwd()}', file=gh_output)


if __name__ == '__main__':
    run()
