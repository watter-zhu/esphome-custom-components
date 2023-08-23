import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import (
    CONF_ID,
    CONF_VOLTAGE,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_VOLTAGE,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_AMPERE,
    UNIT_KILOWATT_HOURS,
    UNIT_VOLT,
    UNIT_WATT,
)

DEPENDENCIES = ["uart"]
AUTO_LOAD = ["bl0939w"]


CONF_CURRENT_3 = "CURRENT_3"
CONF_CURRENT_4 = "CURRENT_4"
CONF_active_power_3 = "active_power_3"
CONF_active_power_4 = "active_power_4"
CONF_energy_3 = "energy_3"
CONF_energy_4 = "energy_4"
CONF_ENERGY_TOTAL2 = "ENERGY_TOTAL2"

bl0939w_ns = cg.esphome_ns.namespace("bl0939w")
bl0939w = bl0939w_ns.class_("bl0939w", cg.PollingComponent, uart.UARTDevice)

CONFIG_SCHEMA = (
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(bl0939w),
            cv.Optional(CONF_VOLTAGE): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_VOLTAGE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENT_3): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_CURRENT_4): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_active_power_3): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_active_power_4): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_energy_3): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_energy_4): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
            cv.Optional(CONF_ENERGY_TOTAL2): sensor.sensor_schema(
                unit_of_measurement=UNIT_KILOWATT_HOURS,
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_ENERGY,
                state_class=STATE_CLASS_TOTAL_INCREASING,
            ),
        }
    )
    .extend(cv.polling_component_schema("60s"))
    .extend(uart.UART_DEVICE_SCHEMA)
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    if voltage_config := config.get(CONF_VOLTAGE):
        sens = await sensor.new_sensor(voltage_config)
        cg.add(var.set_voltage_sensor(sens))
    if CURRENT_3_config := config.get(CONF_CURRENT_3):
        sens = await sensor.new_sensor(CURRENT_3_config)
        cg.add(var.set_current_sensor_1(sens))
    if CURRENT_4_config := config.get(CONF_CURRENT_4):
        sens = await sensor.new_sensor(CURRENT_4_config)
        cg.add(var.set_current_sensor_2(sens))
    if active_power_3_config := config.get(CONF_active_power_3):
        sens = await sensor.new_sensor(active_power_3_config)
        cg.add(var.set_power_sensor_1(sens))
    if active_power_4_config := config.get(CONF_active_power_4):
        sens = await sensor.new_sensor(active_power_4_config)
        cg.add(var.set_power_sensor_2(sens))
    if energy_3_config := config.get(CONF_energy_3):
        sens = await sensor.new_sensor(energy_3_config)
        cg.add(var.set_energy_sensor_1(sens))
    if energy_4_config := config.get(CONF_energy_4):
        sens = await sensor.new_sensor(energy_4_config)
        cg.add(var.set_energy_sensor_2(sens))
    if ENERGY_TOTAL2_config := config.get(CONF_ENERGY_TOTAL2):
        sens = await sensor.new_sensor(ENERGY_TOTAL2_config)
        cg.add(var.set_energy_sensor_sum(sens))
