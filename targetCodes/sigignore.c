//sigignore
#include <signal.h>
#include <stdint.h>
int target(uint8_t **data) {
	sigignore(data[0][0]);
	return 0;
}