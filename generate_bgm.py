import math
import wave
import struct
import random

def generate_ds3_bgm(output_path, duration=150.0, sample_rate=44100):
    total_samples = int(duration * sample_rate)
    samples = [0.0] * total_samples

    # 1. Distant Cathedral Bell tolling at intervals (0s, 24s, 50s, 78s, 105s, 130s)
    bell_times = [1.0, 26.0, 52.0, 78.0, 104.0, 130.0]
    bell_base_freq = 146.83 # D3 deep bronze bell
    bell_partials = [
        (0.5, 0.4, 6.0),   # sub
        (1.0, 0.6, 5.0),   # fundamental
        (1.2, 0.35, 4.0),  # minor third inharmonic
        (1.5, 0.3, 3.5),   # fifth
        (2.0, 0.25, 3.0),  # octave
        (2.6, 0.15, 2.5),  # upper partial
        (3.4, 0.1, 2.0),
    ]

    for bt in bell_times:
        start_idx = int(bt * sample_rate)
        bell_len = int(8.0 * sample_rate)
        for i in range(bell_len):
            idx = start_idx + i
            if idx >= total_samples:
                break
            t = i / sample_rate
            val = 0.0
            for mult, amp, decay in bell_partials:
                freq = bell_base_freq * mult
                env = math.exp(-t * (4.0 / decay))
                val += math.sin(2 * math.pi * freq * t) * amp * env
            samples[idx] += val * 0.35

    # 2. Dark Cello / String Drone in D minor (D2: 73.4Hz, A2: 110Hz, F2: 87.3Hz)
    for i in range(total_samples):
        t = i / sample_rate
        # Breathing LFO
        lfo = 0.85 + 0.15 * math.sin(2 * math.pi * 0.08 * t)
        lfo2 = 0.8 + 0.2 * math.cos(2 * math.pi * 0.05 * t)
        
        # Chord progression very slow: Dm -> Bb -> F -> C -> Dm
        cycle = (t % 32.0)
        if cycle < 12.0:
            f1, f2, f3 = 73.42, 110.0, 87.31 # D, A, F
        elif cycle < 20.0:
            f1, f2, f3 = 58.27, 87.31, 116.54 # Bb, F, Bb
        elif cycle < 26.0:
            f1, f2, f3 = 65.41, 98.00, 130.81 # C, G, C
        else:
            f1, f2, f3 = 73.42, 110.0, 146.83 # D, A, D

        drone = (
            math.sin(2 * math.pi * f1 * t) * 0.22 +
            math.sin(2 * math.pi * f1 * 2 * t) * 0.08 +
            math.sin(2 * math.pi * f2 * t) * 0.15 +
            math.sin(2 * math.pi * f3 * t) * 0.12
        ) * lfo * 0.4
        samples[i] += drone

    # 3. Solitary Poetic Piano / Harp Notes (Soul of Cinder / Gwyn melancholy theme)
    # Notes in D minor: D4(293.66), F4(349.23), A4(440.0), G4(392.0), E4(329.63), C#4(277.18), Bb4(466.16), A3(220)
    piano_pattern = [
        # (time, freq, amp)
        (3.0, 440.0, 0.4),  # A4
        (4.5, 392.0, 0.35), # G4
        (6.0, 349.23, 0.45),# F4
        (9.0, 293.66, 0.5), # D4
        (13.0, 440.0, 0.38),
        (14.5, 349.23, 0.35),
        (16.0, 329.63, 0.4),# E4
        (18.5, 293.66, 0.45),
        
        # Soul of Cinder famous 3 notes motif at climaxes
        (35.0, 493.88, 0.45), # B4
        (36.5, 440.0, 0.4),   # A4
        (38.0, 369.99, 0.48), # F#4
        
        (60.0, 440.0, 0.4),
        (61.5, 392.0, 0.35),
        (63.0, 349.23, 0.45),
        (65.5, 293.66, 0.5),

        (88.0, 493.88, 0.5), # B4
        (89.5, 440.0, 0.45), # A4
        (91.0, 369.99, 0.55), # F#4
        
        (112.0, 440.0, 0.4),
        (114.0, 349.23, 0.4),
        (116.0, 329.63, 0.35),
        (118.0, 293.66, 0.5),
        (122.0, 220.0, 0.4),
        (136.0, 293.66, 0.35),
    ]

    for p_time, freq, amp in piano_pattern:
        start_idx = int(p_time * sample_rate)
        note_dur = int(4.5 * sample_rate)
        for i in range(note_dur):
            idx = start_idx + i
            if idx >= total_samples:
                break
            t = i / sample_rate
            env = math.exp(-t * 1.8) # Natural piano hammer decay
            note_val = (
                math.sin(2 * math.pi * freq * t) * 0.6 +
                math.sin(2 * math.pi * freq * 2.0 * t) * 0.25 +
                math.sin(2 * math.pi * freq * 3.0 * t) * 0.1 +
                math.sin(2 * math.pi * freq * 4.0 * t) * 0.05
            ) * env * amp
            samples[idx] += note_val * 0.3

    # Normalize to -1.5 dB
    max_val = max(abs(s) for s in samples) or 1.0
    norm_factor = 0.65 / max_val

    # Apply fade out at end
    fade_len = int(5.0 * sample_rate)
    for i in range(fade_len):
        idx = total_samples - fade_len + i
        samples[idx] *= (fade_len - i) / fade_len

    with wave.open(output_path, 'wb') as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        out_bytes = bytearray()
        for s in samples:
            val = s * norm_factor
            int_val = int(max(min(val, 0.99), -0.99) * 32767)
            # Subtle stereo width by panning slightly
            out_bytes.extend(struct.pack('<hh', int_val, int_val))
        wf.writeframes(out_bytes)
    print("BGM generated successfully:", output_path)

if __name__ == '__main__':
    generate_ds3_bgm('/Users/sym/Code/dark-souls-3-lore/assets/audio/bgm_dark_souls.wav', duration=150.0)
