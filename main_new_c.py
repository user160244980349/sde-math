#!/usr/bin/env python
import logging
from datetime import datetime

from tools.new_c import Task, thread_c3, thread_c4, thread_c5, thread_writer


def main():
    logging.basicConfig(level=logging.INFO)

    filename = f"c_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.csv"
    logging.info(f"C_Generator: Writing to file {filename}")

    buffer = []

    writer = Task(thread_writer, (buffer, filename), sync=False)
    writer.start()

    Task(thread_c3, (buffer, 51, 56, (0, 0, 0)))
    # Task(thread_c3, (buffer, 0, 50, (0, 0, 0)))

    # Task(thread_c2, (buffer, 0, 15, (0, 1)))
    # Task(thread_c2, (buffer, 0, 15, (1, 0)))
    # Task(thread_c4, (buffer, 0, 15, (0, 0, 0, 0)))

    # Task(thread_c3, (buffer, 0, 6, (0, 0, 1)))
    # Task(thread_c3, (buffer, 0, 6, (0, 1, 0)))
    # Task(thread_c3, (buffer, 0, 6, (1, 0, 0)))
    # Task(thread_c5, (buffer, 0, 6, (0, 0, 0, 0, 0)))

    # Task(thread_c2, (buffer, 0, 2, (0, 2)))
    # Task(thread_c2, (buffer, 0, 2, (1, 1)))
    # Task(thread_c2, (buffer, 0, 2, (2, 0)))
    # Task(thread_c4, (buffer, 0, 2, (0, 0, 0, 1)))
    # Task(thread_c4, (buffer, 0, 2, (0, 0, 1, 0)))
    # Task(thread_c4, (buffer, 0, 2, (0, 1, 0, 0)))
    # Task(thread_c4, (buffer, 0, 2, (1, 0, 0, 0)))
    # Task(thread_c5, (buffer, 0, 2, (0, 0, 0, 0, 0)))
    # Task(thread_c6, (buffer, 0, 2, (0, 0, 0, 0, 0, 0)))

    writer.stop()

    logging.info("Generation has been done")


if __name__ == "__main__":
    main()
