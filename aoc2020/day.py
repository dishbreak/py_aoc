import importlib
import sys


def main() -> None:
    args = sys.argv[1:]
    if len(args) != 1:
        print("expected exactly 1 argument", file=sys.stderr)
        sys.exit(1)
    try:
        day_num = int(args[0])
    except ValueError:
        print("non-numeric argument", file=sys.stderr)
        sys.exit(1)
    module_path = f"day.day{day_num:02d}"
    print(f"loading module {module_path}")
    module = importlib.import_module(module_path)
    module.main()

if __name__ == "__main__":
    main()
