# Reconnaissance Report: addon.so (Zero-MCP leanrea Fast-Path)

## 1. Artifact Classification
* **Magic / Target**: ELF 64-bit LSB shared object (x86-64)
* **SHA-256**: `f086401ffa15f588fa97f088bf1d0e3221e4158185a8bdeca45e2d7319093d5f`
* **Original Preserved**: `true` (work executed strictly on `output/work_copy/addon.so`)

## 2. Technical Findings
1. **Exported Function**: `init_hermes_lock` (seen, `nm -D output/work_copy/addon.so` offset `0x3b0`)
2. **Environment Auth Gate**: `HERMES_TCC_AUTH` (seen, `strings -t x output/work_copy/addon.so` offset `0x1298`)
3. **UNIX Socket Wire Path**: `/tmp/hermes_addon_v2_%d.sock` (seen, `strings -t x output/work_copy/addon.so` offset `0x12a8`)
