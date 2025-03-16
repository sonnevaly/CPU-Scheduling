CPU Scheduling Simulator

Description

This project simulates four CPU scheduling algorithms:

First-Come, First-Served (FCFS)

Shortest-Job-First (SJF)

Shortest-Remaining-Time (SRT)

Round Robin (RR)

The simulator takes user input for processes, including process ID, arrival time, and burst time. It displays the Gantt chart, waiting times, turnaround times, and calculates the average waiting and turnaround times for each algorithm.

How to Run the Program

Prerequisites

Python 3 installed on your system.

Steps

Clone the Repository:

git clone <repository_url>
cd CPU-Scheduling-Simulator

Run the Program:

python cpu_scheduling_simulator.py

Select an Algorithm:
The program will prompt you to select from the following options:

1: First-Come, First-Served (FCFS)

2: Shortest-Job-First (SJF)

3: Shortest-Remaining-Time (SRT)

4: Round Robin (RR)

5: Exit

Enter Process Data:
For each process, enter:

Process ID (e.g., P1, P2)

Arrival Time

Burst Time

For Round Robin: Enter the Time Quantum

View Results:
The program outputs the Gantt chart, waiting times, turnaround times, and average statistics.

Example Run

Select an algorithm (1-5): 1
Enter number of processes: 3
Enter Process ID for P1: P1
Enter Arrival Time for P1: 0
Enter Burst Time for P1: 5
Enter Process ID for P2: P2
Enter Arrival Time for P2: 2
Enter Burst Time for P2: 3
Enter Process ID for P3: P3
Enter Arrival Time for P3: 4
Enter Burst Time for P3: 6

Gantt Chart: P1 (0-5) → P2 (5-8) → P3 (8-14)
Waiting Times: [0, 3, 4]
Turnaround Times: [5, 6, 10]
Average Waiting Time: 2.33
Average Turnaround Time: 7.0

Notes

Error handling: The program ensures invalid inputs like negative numbers or non-integer values are caught and prompts the user to re-enter valid data.

Happy scheduling!

