"""Performance profiling and execution timer decorators."""
import time
import functools
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def timing_decorator(func):
    """Measures the elapsed execution time of a callable function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        elapsed = (time.perf_counter() - start) * 1000.0
        logger.info(f"Function [{func.__name__}] finished in {elapsed:.3f} ms")
        return res
    return wrapper

if __name__ == "__main__":
    @timing_decorator
    def demo():
        return [x ** 2 for x in range(50_000)]
    demo()
