
def myrange2(start, stop=None, step=None):

    if stop:
        if step and step > 0:
            assert stop > start

    if stop:
        if step and step < 0:
            assert stop < start

    results = []
    index = 0 if not stop else start
    end = stop if stop else start
    skip = step if step else 1

    while index < end:
        results.append(index)
        index += skip

    return results


def myrange3(start, stop=None, step=None):

    if stop:
        if step and step > 0:
            assert stop > start

    if stop:
        if step and step < 0:
            assert stop < start

    start_point = 0 if not stop else start
    end_point = start if not stop else stop
    skip = step if step else 1

    while start_point < end_point:
        yield start_point
        start_point += skip




