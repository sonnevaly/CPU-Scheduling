def fcfs(processes):
    processes.sort(key=lambda x: x[1])
    time = 0
    waiting_times = []
    turnaround_times = []
    gantt_chart = []
    
    for process in processes:
        pid, arrival, burst = process
        if time < arrival:
            time = arrival
        waiting_times.append(time - arrival)
        time += burst
        turnaround_times.append(time - arrival)
        gantt_chart.append((pid, time - burst, time))
    
    return waiting_times, turnaround_times, gantt_chart


def sjf(processes):
    processes.sort(key=lambda x: (x[1], x[2]))
    time = 0
    waiting_times = []
    turnaround_times = []
    gantt_chart = []
    
    for process in processes:
        pid, arrival, burst = process
        if time < arrival:
            time = arrival
        waiting_times.append(time - arrival)
        time += burst
        turnaround_times.append(time - arrival)
        gantt_chart.append((pid, time - burst, time))
    
    return waiting_times, turnaround_times, gantt_chart


def srt(processes):
    time = 0
    completed = 0
    n = len(processes)
    remaining_times = [p[2] for p in processes]
    waiting_times = [0] * n
    turnaround_times = [0] * n
    gantt_chart = []
    
    while completed < n:
        shortest = -1
        min_time = float('inf')
        for i in range(n):
            if processes[i][1] <= time and remaining_times[i] < min_time and remaining_times[i] > 0:
                min_time = remaining_times[i]
                shortest = i
        
        if shortest == -1:
            time += 1
            continue
        
        remaining_times[shortest] -= 1
        gantt_chart.append((processes[shortest][0], time, time + 1))
        time += 1

        if remaining_times[shortest] == 0:
            completed += 1
            turnaround_times[shortest] = time - processes[shortest][1]
            waiting_times[shortest] = turnaround_times[shortest] - processes[shortest][2]
    
    return waiting_times, turnaround_times, gantt_chart


def round_robin(processes, quantum):
    queue = processes[:]
    time = 0
    waiting_times = {p[0]: 0 for p in processes}
    turnaround_times = {p[0]: 0 for p in processes}
    gantt_chart = []
    remaining_burst = {p[0]: p[2] for p in processes}
    
    while queue:
        pid, arrival, burst = queue.pop(0)
        if time < arrival:
            time = arrival
        execute_time = min(quantum, remaining_burst[pid])
        gantt_chart.append((pid, time, time + execute_time))
        time += execute_time
        remaining_burst[pid] -= execute_time

        if remaining_burst[pid] > 0:
            queue.append((pid, arrival, burst))
        else:
            turnaround_times[pid] = time - arrival
            waiting_times[pid] = turnaround_times[pid] - burst
    
    return list(waiting_times.values()), list(turnaround_times.values()), gantt_chart


# Menu-driven program

def main():
    while True:
        print("\nCPU Scheduling Simulator")
        print("1. First-Come, First-Served (FCFS)")
        print("2. Shortest-Job-First (SJF)")
        print("3. Shortest-Remaining-Time (SRT)")
        print("4. Round Robin (RR)")
        print("5. Exit")
        
        choice = input("Select an algorithm (1-5): ")
        
        if choice == '5':
            break
        
        num_processes = int(input("Enter number of processes: "))
        processes = []
        for i in range(num_processes):
            pid = input(f"Enter Process ID for P{i+1}: ")
            arrival = int(input(f"Enter Arrival Time for {pid}: "))
            burst = int(input(f"Enter Burst Time for {pid}: "))
            processes.append((pid, arrival, burst))
        
        if choice == '1':
            waiting_times, turnaround_times, gantt_chart = fcfs(processes)
        elif choice == '2':
            waiting_times, turnaround_times, gantt_chart = sjf(processes)
        elif choice == '3':
            waiting_times, turnaround_times, gantt_chart = srt(processes)
        elif choice == '4':
            quantum = int(input("Enter Time Quantum: "))
            waiting_times, turnaround_times, gantt_chart = round_robin(processes, quantum)
        else:
            print("Invalid choice. Please select again.")
            continue
        
        print("\nGantt Chart:", ' → '.join([f"{p[0]} ({p[1]}-{p[2]})" for p in gantt_chart]))
        print("Waiting Times:", waiting_times)
        print("Turnaround Times:", turnaround_times)
        print("Average Waiting Time:", sum(waiting_times) / num_processes)
        print("Average Turnaround Time:", sum(turnaround_times) / num_processes)

if __name__ == "__main__":
    main()
