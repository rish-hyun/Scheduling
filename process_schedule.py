import fcfs as ff
import round_robin as rr

class ProcessSchedule:

    def __init__(self):
        self.schedule_algo = {
            'FCFS': ff.FCFS,
            'Round Robin': rr.RoundRobin,
        }

    def num_of_process(self, total_process):
        self.total_process = total_process

    def get_arrival_time(self):
        self.arrival_time_list = self.get_time('Arrival Time')

    def get_burst_time(self):
        self.burst_time_list = self.get_time('Burst Time')

    def get_time(self, name_time):
        time_list = []
        try:
            for time in range(self.total_process):
                time_list.append(input(f'Process {time} {name_time} : '))
            return time_list
        except:
            raise ValueError('NUMBER OF PROCESS IS NOT KNOWN !!')

    def run(self, option):
        self.schedule_algo.get(option)()
