//tcdrain
#include <termios.h>
#include <stdint.h>
int target(uint8_t **data) {
	tcdrain(data[0][0]);
	return 0;
}