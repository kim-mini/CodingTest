from collections import deque

count = 5
cardQueue = deque(i for i in range(1,count))

for i in range(count):
    if cardQueue[0] == cardQueue[-1]:
        break
    cardQueue.popleft()
    cardQueue.append(cardQueue.popleft())

print(cardQueue)
