try:
    n=int(input())
except ValueError:
    print('value error')
except EOFError:
    print('error')
except KeyboardInterrupt:
    print('caught KeyboardInterrupt')

