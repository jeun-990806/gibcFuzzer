//access
#include <stdint.h>
#include <unistd.h>
#include <fcntl.h>
char tracer[256] = "/sys/kernel/debug/tracing/tracing_on";
char marker[256] = "/sys/kernel/debug/tracing/trace_marker";

int target(uint8_t **data) {
	int trace_fd = open(tracer, O_WRONLY);
	int marker_fd = open(marker, O_WRONLY);
	if(trace_fd >= 0 && marker_fd >= 0){ 
		write(trace_fd, "1", 1);
		write(marker_fd, "start\n", 7);
		access(data[0], data[1][0]);
		write(marker_fd, "end\n", 5);
		write(trace_fd, "0", 1);
	}	return 0;
}