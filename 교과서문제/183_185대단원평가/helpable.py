import sys

if len(sys.argv) == 2:
    if sys.argv[1] == '--help' or sys.argv[1] == '-h':
        print('도움말 : --help나 -h 옵션을 사용하면 도움말을 볼 수 있어요!')
        sys.exit()
print("안녕하세요!")