from machine import Pin, ADC, PWM
from time import sleep
from utils import map_value

# Configura o LED Verde (D10) com PWM
led_verde = PWM(Pin(10))
led_verde.freq(1000)

# Configura o LDR (GPIO 1)
ldr = ADC(Pin(1))
ldr.atten(ADC.ATTN_11DB)
ldr.width(ADC.WIDTH_12BIT)

print("Iluminação Inteligente com PWM Iniciada...")

while True:
    valor_ldr = ldr.read()
    
    # Mapeia leitura do LDR (0 a 4095) para o ciclo de trabalho do PWM (0 a 1023)
    # Relação inversa: quanto menos luz externa, mais forte brilha o LED
    brilho = map_value(valor_ldr, 0, 4095, 1023, 0)
    
    led_verde.duty(brilho)
    
    print("LDR (Luz): {} | Brilho LED (PWM): {}".format(valor_ldr, brilho))
    sleep(0.05)
