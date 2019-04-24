from typing import List


class Job(object):
    def __init__(self, start: int, end: int, value: int):
        self.start = start
        self.end = end
        self.value = value

    def __str__(self):
        return "[" + str(self.start) + ":" + str(self.end) + "]:" + str(self.value)


def get_last_compatible_job(jobs: List[Job], i: int)->int or None:
    """
    :param jobs: a set of requests i...n such as each job j has start, finish, and name
    :param i: the index of the current job
    :return: None if there is no compatible job, else return the last compatible job
    """
    for j in range(i-1, -1, -1):
        # return jobs[j] if its finishing time <= jobs[i].start
        if jobs[j].end <= jobs[i].start:
            return j
    # if no valid job is found, returns 0
    return None


def recursive_wis(jobs: List[Job])->int:
    """
    :jobs: set R of requests i...n such as each job j has start, finish, and name
    :return: set S of compatible requests such as the sum of their values is maximized
    """
    # sort by finishing time
    jobs.sort(key=lambda job: job.end)
    P = []
    for i in range(len(jobs)):
        P.append(get_last_compatible_job(jobs, i))

    def get_opt(j):
        if not j:
            return 0
        else:
            return max(get_opt(j - 1), jobs[j].value + get_opt(P[j]))
    return get_opt(len(jobs) - 1)


def memoized_wis(jobs: List[Job])->int:
    jobs.sort(key=lambda job: job.end)
    P = []
    for i in range(len(jobs)):
        P.append(get_last_compatible_job(jobs, i))
    opt = [None for _ in range(len(jobs))]

    def get_opt(j):
        if not j:
            return 0
        if opt[j]:
            return opt[j]
        else:
            return max(get_opt(j-1), jobs[j].value + get_opt(P[j]))
    return get_opt(len(jobs) - 1)


def dynamic_wis(jobs: List[Job])->tuple:
    jobs.sort(key=lambda job: job.end)
    P = []
    for i in range(len(jobs)):
        P.append(get_last_compatible_job(jobs, i))
    opt = [None for _ in range(len(jobs) + 1)]
    opt[0] = 0
    solution = []

    def find_solution(j):
        """
        :param j:
        :return: print out the solution
        """
        if j is None:
            pass
        else:
            opt1 = opt[j - 1]

            vj = jobs[j - 1].value
            if P[j - 1] is None:
                opt2 = vj
            else:
                opt2 = opt[P[j - 1] + 1] + vj
            if opt2 > opt1:
                solution.append(j)
                try:
                    find_solution(P[j - 1] + 1)
                except TypeError:
                    # handle the case when P[j - 1] == None
                    pass
            else:
                find_solution(j - 1)

    # j is the length of item we search
    for j in range(1, len(jobs) + 1):
        vj = jobs[j - 1].value
        opt1 = opt[j-1]
        if P[j - 1] is None:
            opt2 = vj
        else:
            opt2 = opt[P[j - 1] + 1] + vj
        opt[j] = max(opt1, opt2)
        # opt[j] = max(opt[j-1], jobs[j - 1].name + opt[P[j - 1]])

    find_solution(8)
    return opt[- 1], solution
