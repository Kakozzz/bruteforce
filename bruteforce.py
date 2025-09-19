import time
import matplotlib.pyplot as plt

password = "cumA"
lowercase = "abcdefghijklmnopqrstuvwxyz"
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
all_chars = lowercase + uppercase + numbers
max_length = 4

attempts = 0
found = False
global_start_time = None

attempts_record = []
times_record = []
lengths_record = []
alphabet_size_record = []

def should_record(attempt_count):
    if attempt_count <= 10:
        return True
    if attempt_count <= 100:
        return (attempt_count % 10 == 0)
    if attempt_count <= 1000:
        return (attempt_count % 100 == 0)
    if attempt_count <= 10000:
        return (attempt_count % 1000 == 0)
    return (attempt_count % 5000 == 0)

def record_sample(length, alphabet_size):
    elapsed = time.time() - global_start_time
    attempts_record.append(attempts)
    times_record.append(elapsed)
    lengths_record.append(length)
    alphabet_size_record.append(alphabet_size)

def generate_passwords(chars, length):
    global attempts, found
    indices = [0] * length
    base = len(chars)

    while True:
        guess = "".join(chars[i] for i in indices)
        attempts += 1

        if should_record(attempts):
            record_sample(length=length, alphabet_size=base)

        if guess == password:
            found = True
            record_sample(length=length, alphabet_size=base)
            return

        pos = length - 1
        while pos >= 0:
            indices[pos] += 1
            if indices[pos] == base:
                indices[pos] = 0
                pos -= 1
            else:
                break
        else:
            return

global_start_time = time.time()

for length in range(1, max_length + 1):
    if found:
        break
    generate_passwords(all_chars, length)

total_time = time.time() - global_start_time
if found:
    print(f"\nContraseña encontrada: {password}")
else:
    print("\nContraseña NO encontrada")

print(f"Intentos totales: {attempts:,}")
print(f"Tiempo total: {total_time:.4f} s")

plt.figure(figsize=(10,6))
plt.plot(attempts_record, times_record, marker='o', linestyle='-', linewidth=1, markersize=4, color='tab:blue')
plt.title("Crecimiento exponencial del tiempo vs intentos")
plt.xlabel("Número de intentos (escala logarítmica)")
plt.ylabel("Tiempo transcurrido (segundos)")
plt.grid(True, linestyle='--', linewidth=0.6)
plt.xscale("log")
ax = plt.gca()
ax.yaxis.get_major_formatter().set_useOffset(False)
plt.tight_layout()
plt.show()
