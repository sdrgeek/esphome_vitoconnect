import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor
from esphome.const import CONF_ADDRESS, CONF_LENGTH, CONF_OPTIONS

from .. import CONF_VITOCONNECT_ID, VitoConnect, vitoconnect_ns

DEPENDENCIES = ["vitoconnect"]
OPTOLINKSensor = vitoconnect_ns.class_("OPTOLINKSensor", sensor.Sensor)

OPTIONS_SCHEMA = cv.Schema({
    cv.Required("value"): cv.int_,
    cv.Required("label"): cv.string,
})

CONFIG_SCHEMA = sensor.sensor_schema(OPTOLINKSensor).extend(
    {
        cv.GenerateID(): cv.declare_id(OPTOLINKSensor),
        cv.GenerateID(CONF_VITOCONNECT_ID): cv.use_id(VitoConnect),
        cv.Required(CONF_ADDRESS): cv.uint16_t,
        cv.Required(CONF_LENGTH): cv.uint8_t,
        cv.Optional(CONF_OPTIONS): cv.ensure_list(OPTIONS_SCHEMA),
    }
)


async def to_code(config):
    # Extract labels from options if provided, otherwise use empty list
    if CONF_OPTIONS in config:
        labels = [o["label"] for o in config[CONF_OPTIONS]]
        values = [o["value"] for o in config[CONF_OPTIONS]]
    else:
        labels = []
        values = []

    var = await sensor.new_sensor(config)

    # Add configuration to datapoint
    cg.add(var.setAddress(config[CONF_ADDRESS]))
    cg.add(var.setLength(config[CONF_LENGTH]))

    # Pass labels and numeric values to the C++ class for mapping
    cg.add(var.set_option_labels(labels))
    cg.add(var.set_option_values(values))

    # Add sensor to component hub (VitoConnect)
    hub = await cg.get_variable(config[CONF_VITOCONNECT_ID])
    cg.add(hub.register_datapoint(var))
