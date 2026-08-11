#pragma once

#include "esphome/components/sensor/sensor.h"
#include "../vitoconnect_datapoint.h"

namespace esphome {
namespace vitoconnect {

class OPTOLINKSensor : public sensor::Sensor, public Datapoint {

  public:
    OPTOLINKSensor();
    ~OPTOLINKSensor();

    void decode(uint8_t* data, uint8_t length, Datapoint* dp = nullptr) override;
    void encode(uint8_t* raw, uint8_t length, void* data) override;
    void encode(uint8_t* raw, uint8_t length, float data);
    void setBitMask(uint32_t bit_mask);

  private:
    uint32_t _bit_mask;
};

}  // namespace vitoconnect
}  // namespace esphome