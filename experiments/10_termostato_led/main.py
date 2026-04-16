from machine import Pin, ADC
from time import sleep

LIMIAR = 30.0  # °C — abaixo: LED azul; acima: LED vermelho

lm35 = ADC(Pin(1))
lm35.atten(ADC.ATTN_11DB)
lm35.width(ADC.WIDTH_12BIT)

led_D12 = Pin(12, Pin.OUT)  # azul  — temperatura ok
led_D13 = Pin(13, Pin.OUT)  # vermelho — temperatura alta

print("Termostato pronto. Limiar: {:.1f} °C".format(LIMIAR))

while True:
    leitura = lm35.read()
    tensao = (leitura / 4095) * 3.3
    temperatura = tensao / 0.01  # LM35: 10 mV por °C

    if temperatura > LIMIAR:
        led_D13.on()
        led_D12.off()
        estado = "ALTA"
    else:
        led_D12.on()
        led_D13.off()
        estado = "OK"

    print("Temp: {:.2f} °C | {}".format(temperatura, estado))
    sleep(1)
