from collections import deque


def search(lines, pattern, history=3):
    previous_lines = deque(maxlen=history)
    for li in lines:
        if pattern in li:
            yield li, previous_lines
            previous_lines.append(li)


if __name__ == '__main__':
    # queue
    queue = deque([1, 2, 3], maxlen=2)
    print queue
    queue.append(4)
    # print queue.pop()
    print queue.popleft()
    print queue
    print '-' * 50

    # stack
    # stack = deque([1, 2, 3])
    # print stack
    # stack.append(4)
    # print stack.pop()
    # print '-' * 50

    with open('files/1_3.txt') as f:
        for line, prevlines in search(f, 'python'):
            print ('line:', line)
            print ('prevlines:', prevlines)
            print '-' * 20

        f.seek(0)
        print '-' * 50

        prev_lines = deque(maxlen=3)
        for line in f:
            if 'python' in line:
                prev_lines.append(line)
                print ('prev_lines:', prev_lines)
    f.close()
