#ifndef SENSOR_DATA_H
#define SENSOR_DATA_H

typedef struct {
    float speed_kmh;
    float distance_m;
    float temperature_c;
} SensorData;

void generate_sensor_data(SensorData* data);
void update_speed(SensorData* data);
float get_acceleration_value(void);

#endif
