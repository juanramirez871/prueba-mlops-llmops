import argparse
from funciones import sumar, multiplicar


def main() -> None:
    parser = argparse.ArgumentParser(prog="main")
    parser.add_argument("x", type=float)
    parser.add_argument("y", type=float)
    parser.add_argument("--op", choices=["sumar", "multiplicar"], default="sumar")
    args = parser.parse_args()
    if args.op == "sumar":
        r = sumar(args.x, args.y)
    else:
        r = multiplicar(args.x, args.y)
    print(r)


if __name__ == "__main__":
    main()
