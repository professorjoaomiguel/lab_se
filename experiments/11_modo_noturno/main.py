from machine import Pin, ADC, PWM
from time import sleep

ldr = ADC(Pin(1))
ldr.atten(ADC.ATTN_11DB)
ldr.width(ADC.WIDTH_12BIT)

led = PWM(Pin(10))  # LED verde do RGB
led.freq(1000)

print("Modo noturno pronto. Cubra o LDR para aumentar o brilho.")

while True:
    valor = ldr.read()  # 0 (escuro) – 4095 (muito iluminado)

    # Relação inversa: quanto menos luz, maior o brilho do LED
    brilho = int((1 - valor / 4095) * 1023)
    led.duty(brilho)

    print("LDR:", valor, "| Brilho:", brilho)
    sleep(0.1)
