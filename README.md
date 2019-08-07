# KQ: Asynchronous Task Queue using Kafka

KQ is a simple Python library for queueing tasks to Kafka. These task are processed asynchronously by workers.

KQ currently supports enqueueing any arbitrary python function.

## Requirements

- Python 3.7+
- Apache Kafka 0.10+

### Installation

```bash
pip install async-kq
```

## Getting Started



### Create a Task

```python
def test_fn(x):
    print(x)
```

### Create a new Queue for the Task

```python
from kq.queue import Queue
q = Queue(topic="my-topic", broker=["localhost:9092"])
```

### Enqueue the task

```python
q.enqueue(task=task,args=[10])
```

### Running a worker

```bash
kq --topic my-topic --group-id my-test-group --brokers localhost:9092


Starting a worker with the following args: my-topic, test-group-id, ('localhost:9092',)

Executing Task: fn: task, args: [10], kwargs: {}
10

```

