"use strict";
function utf8(text) {
  if (typeof text !== "string") throw new TypeError("expected string");
  const out = [];
  for (let i = 0; i < text.length; i++) {
    let n = text.charCodeAt(i);
    if (n >= 0xd800 && n <= 0xdbff) {
      const low = text.charCodeAt(++i);
      if (!(low >= 0xdc00 && low <= 0xdfff)) throw new Error("unpaired surrogate");
      n = 0x10000 + ((n - 0xd800) << 10) + low - 0xdc00;
    } else if (n >= 0xdc00 && n <= 0xdfff) throw new Error("unpaired surrogate");
    if (n < 0x80) out.push(n);
    else if (n < 0x800) out.push(0xc0 | (n >> 6), 0x80 | (n & 63));
    else if (n < 0x10000) out.push(0xe0 | (n >> 12), 0x80 | ((n >> 6) & 63), 0x80 | (n & 63));
    else out.push(0xf0 | (n >> 18), 0x80 | ((n >> 12) & 63), 0x80 | ((n >> 6) & 63), 0x80 | (n & 63));
  }
  return Uint8Array.from(out);
}
function sha256(input) {
  const k = [
    0x428a2f98,0x71374491,0xb5c0fbcf,0xe9b5dba5,0x3956c25b,0x59f111f1,0x923f82a4,0xab1c5ed5,
    0xd807aa98,0x12835b01,0x243185be,0x550c7dc3,0x72be5d74,0x80deb1fe,0x9bdc06a7,0xc19bf174,
    0xe49b69c1,0xefbe4786,0x0fc19dc6,0x240ca1cc,0x2de92c6f,0x4a7484aa,0x5cb0a9dc,0x76f988da,
    0x983e5152,0xa831c66d,0xb00327c8,0xbf597fc7,0xc6e00bf3,0xd5a79147,0x06ca6351,0x14292967,
    0x27b70a85,0x2e1b2138,0x4d2c6dfc,0x53380d13,0x650a7354,0x766a0abb,0x81c2c92e,0x92722c85,
    0xa2bfe8a1,0xa81a664b,0xc24b8b70,0xc76c51a3,0xd192e819,0xd6990624,0xf40e3585,0x106aa070,
    0x19a4c116,0x1e376c08,0x2748774c,0x34b0bcb5,0x391c0cb3,0x4ed8aa4a,0x5b9cca4f,0x682e6ff3,
    0x748f82ee,0x78a5636f,0x84c87814,0x8cc70208,0x90befffa,0xa4506ceb,0xbef9a3f7,0xc67178f2
  ];
  const bytes = new Uint8Array(Math.ceil((input.length + 9) / 64) * 64);
  bytes.set(input); bytes[input.length] = 0x80;
  const bits = input.length * 8;
  const view = new DataView(bytes.buffer);
  view.setUint32(bytes.length - 8, Math.floor(bits / 0x100000000), false);
  view.setUint32(bytes.length - 4, bits >>> 0, false);
  const h = [0x6a09e667,0xbb67ae85,0x3c6ef372,0xa54ff53a,0x510e527f,0x9b05688c,0x1f83d9ab,0x5be0cd19];
  const rr = (x,n) => (x >>> n) | (x << (32 - n));
  for (let offset = 0; offset < bytes.length; offset += 64) {
    const w = new Uint32Array(64);
    for (let t=0;t<16;t++) w[t] = view.getUint32(offset+t*4,false);
    for (let t=16;t<64;t++) {
      const a=w[t-15], b=w[t-2];
      w[t] = (w[t-16] + (rr(a,7)^rr(a,18)^(a>>>3)) + w[t-7] + (rr(b,17)^rr(b,19)^(b>>>10))) >>> 0;
    }
    let [a,b,c,d,e,f,g,j] = h;
    for (let t=0;t<64;t++) {
      const s = (j + (rr(e,6)^rr(e,11)^rr(e,25)) + ((e&f)^(~e&g)) + k[t] + w[t]) >>> 0;
      const z = ((rr(a,2)^rr(a,13)^rr(a,22)) + ((a&b)^(a&c)^(b&c))) >>> 0;
      j=g; g=f; f=e; e=(d+s)>>>0; d=c; c=b; b=a; a=(s+z)>>>0;
    }
    [a,b,c,d,e,f,g,j].forEach((v,i)=>h[i]=(h[i]+v)>>>0);
  }
  return h.map(n=>n.toString(16).padStart(8,"0")).join("");
}
module.exports = {utf8,sha256};
