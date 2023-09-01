__all__ = ['print_matrix']

def print_matrix(m):
    x = '\n'.join([''.join(['{:6}'.format(item) for item in row]) for row in m])
    print(x)
