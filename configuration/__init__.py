import sys, subprocess
from pip._internal import main as pip_main

def install_pip(package):
    pip_main(['install', package])

def install_conda(package):
    # do conda install -y $pkg; done
    # cmd = f"conda install {package}"
    cmd = f"conda create --name test_env --file {package}"
    try:
        subprocess.check_output(cmd)
    except:
        print(f"{package} can't be run")

if __name__ == '__main__':
    '''i am lazy today so you get bad code here future me'''

    # sys.argv[1] should be "pip_requirement.txt" or "conda_requirement.txt"
    with open(sys.argv[2]) as f:
        if sys.argv[1] == 'pip':
            for line in f:
                install_pip(line)
        #=====================
        #==unfinished work
        #=====================

        #--------fail to run with python code as well as directly type in anaconda prompt
        # > I used the following command cmd
        #           f"conda create --name test_env --file C:\Users\awannaphasch2016\PycharmProjects\my_utility\config\packages requirement\conda_requirements.txt"
        if sys.argv[1] == 'conda':

            # for line in f:
            install_conda(sys.argv[1])
