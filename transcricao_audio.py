import speech_recognition as sr

# Inicializa o reconhecedor de fala
recognizer = sr.Recognizer()

# Função para capturar e transcrever a fala
def capture_and_transcribe():
    with sr.Microphone() as source:
        print("Ajustando para o ruído ambiente... por favor, espere.")
        recognizer.adjust_for_ambient_noise(source, duration=2)  # Ajuste mais longo para melhorar a calibração do ruído
        print("Por favor, fale algo...")

        # Configura tempo de espera para a fala e limite de tempo
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)  # Aguarda por até 5 segundos e aceita frases de até 10 segundos
        except sr.WaitTimeoutError:
            print("Tempo esgotado. Nenhum áudio detectado.")
            return
        except Exception as e:
            print(f"Erro ao capturar áudio: {e}")
            return

        try:
            print("Reconhecendo o que foi dito...")
            # Converte o áudio para texto usando o Google Web Speech API
            text = recognizer.recognize_google(audio, language="pt-BR")
            print(f"Você disse: {text}")
        except sr.UnknownValueError:
            print("Não consegui entender o áudio. Por favor, fale mais claramente.")
        except sr.RequestError as e:
            print(f"Ocorreu um erro na requisição ao serviço de reconhecimento de fala: {e}")
        except Exception as e:
            print(f"Erro inesperado durante o reconhecimento de fala: {e}")

# Loop contínuo sem a interação do usuário
while True:
    capture_and_transcribe()
