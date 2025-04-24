#include "unity.h"
#include "sensor_data.h"

void setUp(void) {}
void tearDown(void) {}

void test_generate_sensor_data_within_bounds(void) {
    SensorData data;
    generate_sensor_data(&data);

    TEST_ASSERT_TRUE(data.speed_kmh >= 0 && data.speed_kmh <= 300);
    TEST_ASSERT_TRUE(data.distance_m >= 0);
    TEST_ASSERT_TRUE(data.temperature_c >= -40 && data.temperature_c <= 125);
}
