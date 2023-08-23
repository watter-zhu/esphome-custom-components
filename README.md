# esphome-custom-components
esphome第三方组件库

telnet
esp8266继电器到主机的开机开关上
利用esp8266的串口和主机主板上的RS232通信，获得linux的远程访问终端

external_components:
  - source: github://ryanh7/esphome-custom-components
    components: [ telnet ]
uart:
  rx_pin: RX
  tx_pin: TX
  baud_rate: 115200
  rx_buffer_size: 1kB

telnet:
  port: 23
