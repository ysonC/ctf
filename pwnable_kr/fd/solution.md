## File Descriptor ##

A file descriptor is a unique identifier or reference that the operating system assigns to a file when it is opened. It allows programs to interact with files, sockets, or other input/output (I/O) resources.


0 = input
1 = output
2 = error

0x1234 = 4660

int fd = atoi( argv[1] ) - 0x123
	
for fd t0 be 0(input), argv[1] need to be 4660.
