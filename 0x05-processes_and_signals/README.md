# 0x05-processes_and_signals
In Bash, processes and signals are essential concepts for managing and controlling running programs. Here's a brief overview of processes and signals in Bash:

## Processes:

A process is an executing instance of a program. When you run a program in Bash, it starts as a separate process.
Each process is assigned a unique process ID (PID) by the operating system, which can be used to identify and manage the process.
You can view the currently running processes on your system using the ps command. For example, ps aux shows detailed information about all processes.

## Signals:

Signals are software interrupts sent to processes to notify them of certain events or to request a specific action.
You can send signals to processes using the kill command. The kill command terminates a process by default but can also be used to send different signals.
Commonly used signals include:
SIGTERM (15): Terminate the process gracefully.
SIGKILL (9): Forcefully terminate the process.
SIGSTOP (19): Stop the process temporarily.
SIGCONT (18): Resume the execution of a stopped process.
To send a signal to a process, you need to know its PID. You can find the PID using the ps command or by using tools like pgrep or pidof.
To send a signal to a process, you can run kill -SIGNAL PID. For example, to terminate a process with PID 1234, you can use kill -SIGTERM 1234.
