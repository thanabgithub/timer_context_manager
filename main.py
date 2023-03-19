import contextlib
import time


@contextlib.contextmanager
def timer():
    """
    Time the execution of a context block.

    Yields:
        start_time (float): The start time of the timer.
    """
    start_time = time.time()
    try:
        yield start_time
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.2f}s")


with timer():
    print("This should take approximately 0.25 seconds")
    time.sleep(0.25)
