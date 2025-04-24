#ifndef CAN_SIM_H
#define CAN_SIM_H

init_can_interface(void);
void encode_sensor_data(const SensorData* data, uint8_t* can_frame);
void send_can_frame(uint8_t* can_frame);


#endif