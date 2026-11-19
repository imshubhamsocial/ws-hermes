#!/usr/bin/env bash
# Automated Updater and Compiler for Hermes llama-server Substrate
set -euo pipefail
BASE="/var/home/imshubhamsocial"
WS="${BASE}/Projects/Workspace/Personal/hermes"
CACHE="${BASE}/.cache/llama_upstream"
CU13="${WS}/.local/lib/python3.13/site-packages/nvidia/cu13"
export PATH="${CU13}/bin:${PATH}"

mkdir -p "$CACHE"
[[ -d "${CACHE}/.git" ]] && git -C "$CACHE" pull --ff-only || git clone --depth 1 https://github.com/ggml-org/llama.cpp.git "$CACHE"

NVML_H="${CU13}/include/nvml.h"
if [[ ! -f "$NVML_H" ]]; then
    printf '#ifndef NVML_H\n#define NVML_H\nextern "C" {\ntypedef struct nvmlDevice_st* nvmlDevice_t;\ntypedef enum { NVML_SUCCESS = 0 } nvmlReturn_t;\ntypedef enum { NVML_BRAND_UNKNOWN = 0, NVML_BRAND_QUADRO = 1, NVML_BRAND_QUADRO_RTX = 10, NVML_BRAND_NVIDIA_RTX = 11 } nvmlBrandType_t;\nnvmlReturn_t nvmlInit_v2(void);\nnvmlReturn_t nvmlShutdown(void);\nnvmlReturn_t nvmlDeviceGetHandleByPciBusId_v2(const char * p, nvmlDevice_t * d);\nnvmlReturn_t nvmlDeviceGetBrand(nvmlDevice_t d, nvmlBrandType_t * t);\n}\n#endif\n' > "$NVML_H"
fi

LFLAGS="-L${CU13}/lib -Wl,-rpath-link,${CU13}/lib"
cmake -S "$CACHE" -B "${CACHE}/build" -G Ninja \
    -DCMAKE_BUILD_TYPE=Release -DGGML_CUDA=ON -DGGML_CUDA_GRAPHS=ON \
    -DCMAKE_CUDA_ARCHITECTURES=86 -DGGML_NATIVE=OFF -DLLAMA_BUILD_SERVER=ON \
    -DLLAMA_BUILD_UI=OFF -DLLAMA_BUILD_TESTS=OFF -DLLAMA_BUILD_EXAMPLES=OFF \
    -DCMAKE_EXE_LINKER_FLAGS="$LFLAGS" -DCMAKE_SHARED_LINKER_FLAGS="$LFLAGS"

cmake --build "${CACHE}/build" --target llama-server -j "$(nproc)"

systemctl --user stop llama-server.service || true
cp "${CACHE}/build/bin/llama-server" "${BASE}/.local/libexec/llama-server.bin"
cp -a "${CACHE}/build/bin"/lib*.so* "${BASE}/.local/lib/llama.cpp/"
systemctl --user start llama-server.service

for i in {1..30}; do
    curl -s http://127.0.0.1:8138/health | grep -q '"status":"ok"' && exit 0
    sleep 2
done
echo "Error: Server health check timed out." >&2
exit 1
