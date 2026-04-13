import struct, zlib, collections

def read_png_pixels(path):
    with open(path, 'rb') as f:
        data = f.read() 
    i = 8
    chunks = {}
    while i < len(data):
        length = struct.unpack('>I', data[i:i+4])[0]
        ctype = data[i+4:i+8].decode('ascii', errors='ignore')
        cdata = data[i+8:i+8+length]
        chunks.setdefault(ctype, []).append(cdata)
        i += 12 + length
    w, h, bd, ct = struct.unpack('>IIBB', chunks['IHDR'][0][:10])
    raw = zlib.decompress(b''.join(chunks['IDAT']))
    channels = {2:3, 6:4, 0:1, 3:3, 4:2}.get(ct, 3)
    pixels = []
    prev = bytes(w * channels)
    idx = 0
    for row in range(h):
        filt = raw[idx]; idx += 1
        row_raw = bytearray(raw[idx:idx + w * channels]); idx += w * channels
        recon = bytearray(w * channels)
        for k in range(w * channels):
            a = recon[k - channels] if k >= channels else 0
            b = prev[k]
            c = prev[k - channels] if k >= channels else 0
            rb = row_raw[k]
            if filt == 0:
                recon[k] = rb
            elif filt == 1:
                recon[k] = (rb + a) & 0xff
            elif filt == 2:
                recon[k] = (rb + b) & 0xff
            elif filt == 3:
                recon[k] = (rb + (a + b) // 2) & 0xff
            elif filt == 4:
                p = a + b - c
                pa, pb, pc = abs(p - a), abs(p - b), abs(p - c)
                pr = a if pa <= pb and pa <= pc else b if pb <= pc else c
                recon[k] = (rb + pr) & 0xff
        prev = bytes(recon)
        for x in range(0, w * channels, channels):
            pixels.append(tuple(recon[x:x+3]))
    return pixels, w, h

pixels, w, h = read_png_pixels('/Users/saiteja-chinthareddy/Documents/dev/school-project/img/background.png')

# Sample every 4th pixel for speed
sampled = pixels[::4]

def bucket(c, s=22):
    return tuple((x // s) * s for x in c[:3])

counts = collections.Counter(bucket(p) for p in sampled)
top = counts.most_common(20)
print(f"Image {w}x{h}, sampled {len(sampled)} pixels")
for color, cnt in top:
    print('#{:02x}{:02x}{:02x}  rgb{}  x{}'.format(*color, color, cnt))

