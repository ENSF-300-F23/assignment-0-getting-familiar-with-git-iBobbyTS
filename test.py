import subprocess
import random


operation_list = ['+', '-', '*', '/']
cmd = ['python', 'main.py']

error = 0
for i in range(1000):
    process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
    a = random.randint(-999, 999)
    b = random.randint(-999, 999)
    c = random.randint(-999, 999)
    o1 = random.choice(operation_list)
    o2 = random.choice(operation_list)
    true_result = eval(f'({a}){o1.replace("/", "//")}({b}){o2.replace("/", "//")}({c})')
    process.stdin.write(f'{a}\n')
    process.stdin.write(f'{o1}\n')
    process.stdin.write(f'{b}\n')
    process.stdin.write(f'{o2}\n')
    process.stdin.write(f'{c}\n')
    process.stdin.flush()
    output = process.communicate()[0]
    output = int(true_result == int(output.split('\n')[1][20:]))
    error += output
    process.stdin.close()
    process.wait()

if error == 0:
    print('All tests passed')
else:
    print(f'{error} tests failed')
