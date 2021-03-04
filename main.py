import process_schedule as ps

# Create ProcessSchule Object
sh = ps.ProcessSchedule()

# Get Number of processes
num = int(input('How many processes are there? : '))

# Send values to object of ProcessSchedule
sh.num_of_process(num)
sh.get_arrival_time()
sh.get_burst_time()

# Select Schedule Algorithm
for option in sh.schedule_algo.keys():
    print(option)
opt = input('Your Option : ')

# Run Selected Scheduling Algorithm
sh.run(opt)
