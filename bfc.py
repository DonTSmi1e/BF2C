import os
import sys


def bf2c(bf_src: str, memory_dump=False):
    """
        [Brainfuck to C]
    bf_src - String containing the source code for Brainfuck
    memory_dump - If True, a Brainfuck memory dump file will be created upon completion of the compiled program.

    Returns a string containing the C source code. Can be compiled using GCC, TCC or any similar compilers.
    (The output source code is quite unoptimized)
    """

    c_src = "#include <stdio.h>\n#include <string.h>\nint main() { int i = 0; char arr[30000]; memset(arr, 0, 30000); "

    for char in bf_src:
        match char:
            case '>':
                c_src += "i++; "
            case '<':
                c_src += "i--; "
            case '+':
                c_src += "arr[i]++; "
            case '-':
                c_src += "arr[i]--; "
            case '.':
                c_src += "putchar(arr[i]); "
            case ',':
                c_src += "arr[i] = getchar(); "
            case '[':
                c_src += "while (arr[i]) { "
            case ']':
                c_src += "} "

    c_src += ('FILE *file = fopen("bf_memory_dump.bin", "w"); fwrite(&arr, sizeof(char), 30000, file); fclose(file); puts("\n----------\nProgram exited, memory dump written in bf_memory_dump.bin"); ' if memory_dump else '') + "return 0; }"

    return c_src


if __name__ == "__main__":
    if len(sys.argv) > 1:
        src_file = sys.argv[1]
        out_file = ''.join(src_file.split('.')[:-1])
        os_executable = ".exe" if os.name == "nt" else ''

        with open(src_file, 'r') as src:
            with open(out_file + ".c", 'w') as out:
                out.write(bf2c(src.read(), True if "-d" in sys.argv else False))

        sys.exit(os.system(f"tcc {out_file + '.c'} -o {out_file + os_executable}") >> 8)
    else:
        print(f"Usage: {sys.argv[0]} <source file>")
        sys.exit(1)

