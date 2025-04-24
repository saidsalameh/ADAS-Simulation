#include "sensor_data.h"
#include <stdlib.h>
#include <time.h>


void update_speed(SensorData* data){

    float accel = get_acceleration_value();

    data->speed_kmh += accel;

    if (data->speed_kmh > 200.0f) data->speed_kmh = 200.0f;
    if (data->speed_kmh < 0.0f) data->speed_kmh = 0.0f;
}

float get_acceleration_value(void) {
    return ((rand() % 1001) / 100.0f) - 5.0f; // range: -5.0 to +5.0
}


void generate_sensor_data(SensorData* data) {
    update_speed(data);

    // Simulate distance as cumulative
    data->distance_m += data->speed_kmh * 0.1f; // assume update every 100ms

    // Clamp distance (optional)
    if (data->distance_m > 500.0f) data->distance_m = 0.0f;

    // Simulate temperature (random small fluctuation)
    float temp_variation = ((rand() % 21) - 10) / 10.0f;
    data->temperature_c += temp_variation;

    // Clamp temperature to -40 to 125
    if (data->temperature_c < -40.0f) data->temperature_c = -40.0f;
    if (data->temperature_c > 125.0f) data->temperature_c = 125.0f;
}
