import logging
import os
import threading
from datetime import datetime

import config as c
from mathematics.sde.nonlinear.c import get_c


class Task:
    def __init__(self, task, args=(), sync=True):
        self.task = task
        self.args = args
        self.sync = sync
        self.running = True
        self.thread = threading.Thread(target=self.task, args=(self, self.args))

        if sync:
            self.thread.start()
            self.thread.join()

    def start(self):
        self.thread.start()

    def stop(self):
        self.running = False
        self.thread.join()


def _store(buffer, file):
    with open(os.path.join(c.resources, file), "a") as f:
        f.write("\n".join(buffer))


def thread_writer(task, args):
    buffer, filename = args
    while task.running:

        if len(buffer) > c.read_buffer_size:
            buffer_to_store = buffer.copy()
            buffer.clear()
            _store(buffer_to_store, filename)

    _store(buffer, filename)


def thread_c2(task, args):
    buffer, start_id, end_id, w = args

    if len(w) != 2:
        logging.error("C_Generator: Bad weight tuple size, expected 2")
        return

    while task.running:

        if start_id > end_id > 0:
            break

        logging.info(f"C_Generator: Started C generation up to {start_id}:{start_id}")
        index = f"{start_id}:{start_id}_{w[0]}:{w[1]}"

        for i in range(start_id + 1):
            for j in range(start_id + 1):
                if i != start_id and j != start_id:
                    continue
                buffer.append(f"\"{i}:{j}_{w[0]}:{w[1]}\";\"{get_c((i, j), w)}\"")

        logging.info(f"C_Generator: Completed {index} on {datetime.now().strftime('%d-%m-%Y %H:%M')}")
        start_id += 1


def thread_c3(task, args):
    buffer, start_id, end_id, w = args

    if len(w) != 3:
        logging.error("C_Generator: Bad weight tuple size, expected 3")
        return

    while task.running:

        if start_id > end_id > 0:
            break

        logging.info(f"C_Generator: Started C generation up to {start_id}:{start_id}:{start_id}")
        index = f"{start_id}:{start_id}:{start_id}_{w[0]}:{w[1]}:{w[2]}"

        for i in range(start_id + 1):
            for j in range(start_id + 1):
                for k in range(start_id + 1):
                    if i != start_id and j != start_id and k != start_id:
                        continue
                    buffer.append(f"\"{i}:{j}:{k}_{w[0]}:{w[1]}:{w[2]}\";\"{get_c((i, j, k), w)}\"")

        logging.info(f"C_Generator: Completed {index} on {datetime.now().strftime('%d-%m-%Y %H:%M')}")
        start_id += 1


def thread_c4(task, args):
    buffer, start_id, end_id, w = args

    if len(w) != 4:
        logging.error("C_Generator: Bad weight tuple size, expected 4")
        return

    while task.running:

        if start_id > end_id > 0:
            break

        logging.info(f"C_Generator: Started C generation up to {start_id}:{start_id}:{start_id}:{start_id}")
        index = f"{start_id}:{start_id}:{start_id}:{start_id}_{w[0]}:{w[1]}:{w[2]}:{w[3]}"

        for i in range(start_id + 1):
            for j in range(start_id + 1):
                for k in range(start_id + 1):
                    for l in range(start_id + 1):
                        if i != start_id and j != start_id and k != start_id and l != start_id:
                            continue
                        buffer.append(f"\"{i}:{j}:{k}:{l}_{w[0]}:{w[1]}:{w[2]}:{w[3]}\";\"{get_c((i, j, k, l), w)}\"")

        logging.info(f"C_Generator: Completed {index} on {datetime.now().strftime('%d-%m-%Y %H:%M')}")
        start_id += 1


def thread_c5(task, args):
    buffer, start_id, end_id, w = args

    if len(w) != 5:
        logging.error("C_Generator: Bad weight tuple size, expected 5")
        return

    while task.running:

        if start_id > end_id > 0:
            break

        logging.info(f"C_Generator: Started C generation up to {start_id}:{start_id}:{start_id}:{start_id}:{start_id}")
        index = f"{start_id}:{start_id}:{start_id}:{start_id}:{start_id}_{w[0]}:{w[1]}:{w[2]}:{w[3]}:{w[4]}"

        for i in range(start_id + 1):
            for j in range(start_id + 1):
                for k in range(start_id + 1):
                    for l in range(start_id + 1):
                        for m in range(start_id + 1):
                            if i != start_id and j != start_id and k != start_id and l != start_id and m != start_id:
                                continue
                            buffer.append(
                                f"\"{i}:{j}:{k}:{l}:{m}_{w[0]}:{w[1]}:{w[2]}:{w[3]}:{w[4]}\";\"{get_c((i, j, k, l, m), w)}\"")

        logging.info(f"C_Generator: Completed {index} on {datetime.now().strftime('%d-%m-%Y %H:%M')}")
        start_id += 1


def thread_c6(task, args):
    buffer, start_id, end_id, w = args

    if len(w) != 6:
        logging.error("C_Generator: Bad weight tuple size, expected 6")
        return

    while task.running:

        if start_id > end_id > 0:
            break

        logging.info(
            f"C_Generator: Started C generation up to {start_id}:{start_id}:{start_id}:{start_id}:{start_id}:{start_id}")
        index = f"{start_id}:{start_id}:{start_id}:{start_id}:{start_id}:{start_id}_{w[0]}:{w[1]}:{w[2]}:{w[3]}:{w[4]}:{w[5]}"

        for i in range(start_id + 1):
            for j in range(start_id + 1):
                for k in range(start_id + 1):
                    for l in range(start_id + 1):
                        for m in range(start_id + 1):
                            for n in range(start_id + 1):
                                if i != start_id and j != start_id and k != start_id and l != start_id and m != start_id and n != start_id:
                                    continue
                                buffer.append(
                                    f"\"{i}:{j}:{k}:{l}:{m}:{n}_{w[0]}:{w[1]}:{w[2]}:{w[3]}:{w[4]}:{w[5]}\";\"{get_c((i, j, k, l, m, n), w)}\"")

        logging.info(f"C_Generator: Completed {index} on {datetime.now().strftime('%d-%m-%Y %H:%M')}")
        start_id += 1