import esolang.level0_arithmetic
import esolang.level1_statements
import esolang.level2_loops
import esolang.level3_functions
import argparse

def run_esolang_file(file, lang):
    parser = lang.parser
    interpreter = lang.Interpreter()

    with open(file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):  # Skip blank lines and comments
                continue
            try:
                tree = parser.parse(line)
                result = interpreter.visit(tree)
                if result is not None:
                    print(result)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Run an esolang file.")
    parser.add_argument('file', type=str, help="Path to the esolang file to execute.")
    parser.add_argument('--level', default=3, type=int, help="Select language level (0-3).")
    args = parser.parse_args()

    if args.level == 0:
        run_esolang_file(args.file, esolang.level0_arithmetic)
    elif args.level == 1:
        run_esolang_file(args.file, esolang.level1_statements)
    elif args.level == 2:
        run_esolang_file(args.file, esolang.level2_loops)
    elif args.level == 3:
        run_esolang_file(args.file, esolang.level3_functions)

