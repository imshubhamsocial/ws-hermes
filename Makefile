# /var/home/imshubhamsocial/Projects/Workspace/Personal/hermes/Makefile
# ws-hermes Distrobox Root Umbrella Automation (Forwards to hermes/devel)

DEVEL_DIR := hermes/devel

.PHONY: all walk-test check-vram-quiescent check-vram-active run-eval gauntlet-a gauntlet-b gauntlet-c run-all-gauntlets phase-58-seal

all:
	$(MAKE) -C $(DEVEL_DIR) all

walk-test:
	$(MAKE) -C $(DEVEL_DIR) walk-test

check-vram-quiescent:
	$(MAKE) -C $(DEVEL_DIR) check-vram-quiescent

check-vram-active:
	$(MAKE) -C $(DEVEL_DIR) check-vram-active

run-eval:
	$(MAKE) -C $(DEVEL_DIR) run-eval

gauntlet-a:
	$(MAKE) -C $(DEVEL_DIR) gauntlet-a

gauntlet-b:
	$(MAKE) -C $(DEVEL_DIR) gauntlet-b

gauntlet-c:
	$(MAKE) -C $(DEVEL_DIR) gauntlet-c

run-all-gauntlets:
	$(MAKE) -C $(DEVEL_DIR) run-all-gauntlets

phase-58-seal:
	$(MAKE) -C $(DEVEL_DIR) phase-58-seal
