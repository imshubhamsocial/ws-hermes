# hermes/devel/Makefile
# Hermes Agent OS Development Track Automation (GDR36 Phase 58)

.PHONY: all walk-test check-vram-quiescent check-vram-active run-eval gauntlet-a gauntlet-b gauntlet-c run-all-gauntlets phase-58-seal

all: walk-test run-all-gauntlets check-vram-quiescent

walk-test:
	python3 _tools/hermes_icm_validator.py

check-vram-quiescent:
	python3 _tools/check_vram_limit.py --mode quiescent --max-quiescent 100.0

check-vram-active:
	python3 _tools/check_vram_limit.py --mode active --max-active 5800.0

run-eval:
	bash phases/phase_54_agent_harness_evaluation_and_128k_realism/03_verify/contract.sh

gauntlet-a:
	bash benchmarks/gauntlet_a_voxel_fps/contract.sh

gauntlet-b:
	python3 _tools/hermes_stage_runner.py --stage-dir stages/01-probe --gate-mode autonomous --verify-only
	python3 _tools/hermes_stage_runner.py --stage-dir stages/02-controller --gate-mode autonomous --verify-only
	python3 _tools/hermes_stage_runner.py --stage-dir stages/03-execute --gate-mode autonomous --verify-only
	bash benchmarks/gauntlet_b_splatbox/contract.sh

gauntlet-c:
	bash benchmarks/gauntlet_c_aquarium/contract.sh

run-all-gauntlets: walk-test gauntlet-a gauntlet-b gauntlet-c

phase-58-seal:
	bash phases/phase_58_autonomous_icm_factory_and_multi_gauntlet_certification/03_verify/contract.sh
