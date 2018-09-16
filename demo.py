import os
from optparse import OptionParser


def execute(path, options):
    print("=" * 20)
    print(path)

    print("Compiling... ", end="")
    output = os.system(
        f"{options.compiler} {path} -o bin{os.sep}demo > /dev/null 2>&1")
    if output == 0:
        print("success!")
    else:
        print("failed!")
        return

    print("-" * 20)
    os.system("bin/demo")


def main():
    try:
        os.mkdir("bin")
    except:
        pass

    parser = OptionParser()
    parser.add_option("-c", "--compiler", dest="compiler", default="g++",
                      help="compiler used to build the demos")

    (options, _) = parser.parse_args()

    for root, _, files in os.walk("src"):
        for file in files:
            execute(f"{root}{os.sep}{file}", options)

    try:
        os.remove("bin/demo")
        os.rmdir("bin")
    except:
        pass


main()
