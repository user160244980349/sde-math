#!/usr/bin/env python
import logging
import os
from datetime import datetime
from multiprocessing import cpu_count, Pool

from config import csv, new_c_portion_size
from mathematics.sde.nonlinear.new_c import thread_c, split_task


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S"
    )
    logger = logging.getLogger(__name__)

    filename = os.path.join(csv, f"c_{datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}.csv")
    logging.info(f"Writing to file {filename}")

    tasks = [
        (((57, 58), (57, 58), (57, 58)), (0, 0, 0)),
        # (((0, 56), (0, 56), (0, 56)), (0, 0, 0)),
        #
        # (((0, 15), (0, 15), (0, 15)), (0, 1)),
        # (((0, 15), (0, 15), (0, 15)), (1, 0)),
        # (((0, 15), (0, 15), (0, 15)), (0, 0, 0, 0)),
        #
        # (((0, 6), (0, 6), (0, 6)), (0, 0, 1)),
        # (((0, 6), (0, 6), (0, 6)), (0, 1, 0)),
        # (((0, 6), (0, 6), (0, 6)), (1, 0, 0)),
        # (((0, 6), (0, 6), (0, 6), (0, 6), (0, 6)), (0, 0, 0, 0, 0)),
        #
        # (((0, 2), (0, 2)), (0, 2)),
        # (((0, 2), (0, 2)), (1, 1)),
        # (((0, 2), (0, 2)), (2, 0)),
        # (((0, 2), (0, 2), (0, 2), (0, 2)), (0, 0, 0, 1)),
        # (((0, 2), (0, 2), (0, 2), (0, 2)), (0, 0, 1, 0)),
        # (((0, 2), (0, 2), (0, 2), (0, 2)), (0, 1, 0, 0)),
        # (((0, 2), (0, 2), (0, 2), (0, 2)), (1, 0, 0, 0)),
        # (((0, 2), (0, 2), (0, 2), (0, 2), (0, 2)), (0, 0, 0, 0, 0)),
        # (((0, 2), (0, 2), (0, 2), (0, 2), (0, 2), (0, 2)), (0, 0, 0, 0, 0, 0)),
    ]

    with Pool(cpu_count()) as p:

        for t in tasks:

            logger.info(f"Running task {t}")

            for chunk in chunks(split_task(t), new_c_portion_size):
                c = p.map(thread_c, chunk)
                c.append("")

                with open(filename, "a") as f:
                    f.write("\n".join(c))
                    f.close()

                logger.info(f"The portion of C has been written {chunk[0]}-{chunk[-1]}")

    logger.info("Generation has been done")


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


if __name__ == "__main__":
    main()
