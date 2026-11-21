# Concurrency

## What Is Concurrency?

**Concurrency** is the ability of a program to manage multiple tasks during overlapping periods of time. Instead of completing one task entirely before starting another, a concurrent program can make progress on several tasks within the same time frame.

Concurrency is primarily about **structuring and managing multiple tasks**, rather than necessarily executing them simultaneously.

For example, imagine a web application that needs to:
- Fetch user information from an API.
- Retrieve a list of products from a database.
- Load user notifications.

A sequential approach would perform these operations one after another. A concurrent approach allows the application to make progress on multiple operations without unnecessarily waiting for each one to finish.

## Concurrency vs. Parallelism

Although these concepts are closely related, they are not interchangeable.

| Concurrency | Parallelism |
|---|---|
| Multiple tasks make progress during overlapping periods. | Multiple tasks execute simultaneously. |
| Focuses on task coordination and management. | Focuses on simultaneous execution. |
| Can happen on a single CPU core. | Requires multiple execution resources, such as CPU cores. |
| Tasks may take turns executing. | Tasks execute at the same time. |

### Example

**Concurrency (single-core CPU):**

Tasks take turns using the processor, allowing multiple tasks to make progress over time.

**Parallelism (multi-core CPU):**

Different processor cores execute different tasks simultaneously.

> Parallelism is one way to achieve concurrency, but concurrency does not necessarily require parallel execution.

## Key Concepts

### 1. Process

A process is an independent instance of a running program.

Each process generally has its own memory space and system resources.

### 2. Thread

A thread is the smallest unit of execution managed by an operating system.

Multiple threads can exist within a single process and share its memory space.

### 3. Multithreading

Multithreading is the execution of multiple threads within a single process.

It allows applications to handle multiple operations efficiently, particularly when tasks spend time waiting for I/O operations.

### 4. Asynchronous Programming

Asynchronous programming allows a program to initiate an operation and continue executing other code without blocking while waiting for that operation to finish.

For example, JavaScript uses asynchronous operations extensively when handling network requests.

### 5. Race Condition

A race condition occurs when multiple threads or tasks access shared data concurrently, and the final result depends on the order in which they execute.

**Example:**

Suppose two threads attempt to increment the same shared variable:

```python
counter = counter + 1
```

If both threads read the same initial value before either writes its result, one update may be lost.

This is known as a race condition.

### 6. Critical Section

A critical section is a part of a program that accesses shared resources and must be protected against unsafe concurrent access.

### 7. Mutual Exclusion (Mutex)

A mutex is a synchronization mechanism that ensures only one thread at a time can access a protected critical section.

### 8. Deadlock

A deadlock occurs when two or more threads become permanently blocked because each is waiting for a resource held by another.

For example:

- Thread A holds Resource 1 and waits for Resource 2.
- Thread B holds Resource 2 and waits for Resource 1.

Neither thread can proceed.

## Synchronization Mechanisms

Synchronization helps coordinate concurrent tasks and prevent inconsistent access to shared resources.

Common mechanisms include:

- **Mutex:** Allows only one thread to access a protected resource at a time.
- **Semaphore:** Controls access to a resource through a limited number of permits.
- **Monitor:** Combines shared data and synchronization operations.
- **Condition Variable:** Allows threads to wait until a particular condition becomes true.
- **Atomic Operations:** Perform certain operations indivisibly, preventing interference from other threads.

## Concurrency in Python

Python provides several tools for working with concurrency:

| Module | Purpose |
|---|---|
| `threading` | Working with multiple threads. |
| `multiprocessing` | Running multiple processes. |
| `asyncio` | Writing asynchronous, event-driven programs. |
| `concurrent.futures` | High-level interfaces for managing thread and process pools. |

Example using threads:

```python
import threading
import time

def task(name):
    print(f"Starting {name}")
    time.sleep(2)
    print(f"Finished {name}")

threads = []

for i in range(3):
    thread = threading.Thread(
        target=task,
        args=(f"Task {i + 1}",)
    )
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All tasks completed!")
```

Here:
- `start()` begins executing a thread.
- `join()` waits for a thread to finish.
- Multiple tasks can make progress during overlapping periods.

**Note:** In standard CPython builds, the Global Interpreter Lock (GIL) limits simultaneous execution of Python bytecode by multiple threads. Threads are still useful for I/O-bound operations. Multiprocessing is commonly used for CPU-bound parallel workloads.

## Why Is Concurrency Important?

Concurrency is important because it helps applications:

- Improve responsiveness.
- Handle multiple users and requests.
- Reduce unnecessary waiting.
- Manage I/O-bound operations efficiently.
- Make better use of available computing resources.
- Build scalable and responsive systems.

However, concurrency also introduces challenges such as race conditions, deadlocks, synchronization overhead, and debugging complexity.

## Concurrency in LeetCode

Concurrency is also an important topic in algorithmic problem-solving and technical interviews.

LeetCode concurrency problems typically test your understanding of:

- Thread synchronization.
- Execution ordering.
- Mutual exclusion.
- Locks and semaphores.
- Conditional waiting.
- Coordinating multiple threads.
- Preventing race conditions.

### Common LeetCode Concurrency Problems

| Problem | Main Concept |
|---|---|
| 1114. Print in Order | Thread synchronization |
| 1115. Print FooBar Alternately | Alternating execution |
| 1116. Print Zero Even Odd | Conditional synchronization |
| 1117. Building H2O | Semaphore and synchronization |
| 1195. Fizz Buzz Multithreaded | Thread coordination |
| 1226. The Dining Philosophers | Deadlock and resource management |

## Learning Roadmap

A suggested order for studying concurrency:

1. Understand processes and threads.
2. Learn the difference between concurrency and parallelism.
3. Understand shared memory and race conditions.
4. Study mutexes, locks, and semaphores.
5. Learn thread synchronization and execution ordering.
6. Understand deadlocks and how to prevent them.
7. Solve LeetCode concurrency problems.

## Further Reading

- [Python Threading Documentation](https://docs.python.org/3/library/threading.html)
- [Python Multiprocessing Documentation](https://docs.python.org/3/library/multiprocessing.html)
- [Python Asyncio Documentation](https://docs.python.org/3/library/asyncio.html)
- [LeetCode Concurrency Problems](https://leetcode.com/problemset/concurrency/)

---

**Key Takeaway:** Concurrency is about managing multiple tasks whose execution overlaps. Understanding synchronization, shared resources, race conditions, and deadlocks is essential to writing correct and efficient concurrent programs.