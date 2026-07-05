from fastapi import FastAPI
import serial
import threading

app = FastAPI()

ultimo_numero = None
ser = None


def leitor_serial():
    global ultimo_numero, ser

    while True:
        try:
            linha = ser.readline()

            texto = linha.decode(errors="ignore").strip()

            if texto.isdigit():
                ultimo_numero = int(texto)
                print(f"Recebido: {ultimo_numero}")

        except Exception as e:
            print("Erro serial:", e)


@app.on_event("startup")
def startup():
    global ser

    ser = serial.Serial(
        "COM7",
        115200,
        timeout=1
    )

    threading.Thread(
        target=leitor_serial,
        daemon=True
    ).start()

    print("Serial conectada")


@app.on_event("shutdown")
def shutdown():
    global ser

    if ser and ser.is_open:
        ser.close()

    print("Serial fechada")


@app.get("/telemetry")
def telemetry():
    return {
        "numero": ultimo_numero
    }