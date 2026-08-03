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

    // setters from Python config
    void set_option_labels(const std::vector<std::string> &labels);
    void set_option_values(const std::vector<uint8_t> &values);
  private:
    std::vector<std::string> option_labels_;
    std::vector<uint8_t> option_values_;
    uint8_t current_value_ = 0;
};

}  // namespace vitoconnect
}  // namespace esphome