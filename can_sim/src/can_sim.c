#include "can_sim.h"
#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <net/if.h>
#include <sys/ioctl.h>
#include <sys/socket.h>
#include <linux/can.h>
#include <linux/can/raw.h>

void init_can_interface(void){
    pintf("[CAN init] : CAN interface initialized (simulated)\n");

}