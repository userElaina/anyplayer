import os


def which(program: str) -> str:
    if os.name == "nt" and not program.lower().endswith(".exe"):
        program += ".EXE"

    envdir_list = [os.curdir] + os.environ["PATH"].split(os.pathsep)

    for envdir in envdir_list:
        program_path = os.path.join(envdir, program)
        if os.path.isfile(program_path) and os.access(program_path, os.X_OK):
            return program_path
