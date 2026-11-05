import * as THREE from 'three';

/**
 * Manages the 32x16x32 voxel arena using THREE.InstancedMesh.
 * @class VoxelWorld
 */
export class VoxelWorld {
    static WORLD_SIZE_X = 32;
    static WORLD_SIZE_Y = 16;
    static WORLD_SIZE_Z = 32;
    static VOXEL_SIZE = 1.0;
    static MAX_VOXELS = VoxelWorld.WORLD_SIZE_X * VoxelWorld.WORLD_SIZE_Y * VoxelWorld.WORLD_SIZE_Z;

    static voxelMesh;
    static instanceColor = new THREE.InstancedBufferAttribute(new Float32Array(VoxelWorld.MAX_VOXELS * 3), 3);
    static voxelData = new Uint8Array(VoxelWorld.MAX_VOXELS).fill(0);

    static init() {
        // 1. Fill ground layer (Y=0)
        for (let x = 0; x < VoxelWorld.WORLD_SIZE_X; x++) {
            for (let z = 0; z < VoxelWorld.WORLD_SIZE_Z; z++) {
                const index = x + z * VoxelWorld.WORLD_SIZE_X;
                const y_index = index + 0 * VoxelWorld.WORLD_SIZE_X * VoxelWorld.WORLD_SIZE_Z;
                VoxelWorld.voxelData[y_index] = 1; // Solid ground
            }
        }

        // 2. Add simple cover bunkers
        const bunkerPositions = [
            { x: 10, z: 12, y: 1 },
            { x: 20, z: 22, y: 1 }
        ];
        bunkerPositions.forEach(pos => {
            for (let dx = -1; dx <= 1; dx++) {
                for (let dz = -1; dz <= 1; dz++) {
                    const x = pos.x + dx;
                    const z = pos.z + dz;
                    if (x >= 0 && x < VoxelWorld.WORLD_SIZE_X && z >= 0 && z < VoxelWorld.WORLD_SIZE_Z) {
                        const index = x + z * VoxelWorld.WORLD_SIZE_X;
                        const y_index = index + 1 * VoxelWorld.WORLD_SIZE_X * VoxelWorld.WORLD_SIZE_Z;
                        VoxelWorld.voxelData[y_index] = 2; // Bunker
                    }
                }
            }
        });

        // 3. Build InstancedMesh
        const boxGeometry = new THREE.BoxGeometry(VoxelWorld.VOXEL_SIZE, VoxelWorld.VOXEL_SIZE, VoxelWorld.VOXEL_SIZE);
        const material = new THREE.MeshStandardMaterial({ color: 0x888888 });
        
        VoxelWorld.voxelMesh = new THREE.InstancedMesh(boxGeometry, material, VoxelWorld.MAX_VOXELS);
        VoxelWorld.voxelMesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage);
        VoxelWorld.voxelMesh.instanceColor = VoxelWorld.instanceColor;
        
        // Populate instances
        let count = 0;
        for (let i = 0; i < VoxelWorld.MAX_VOXELS; i++) {
            if (VoxelWorld.voxelData[i] !== 0) {
                const x = i % VoxelWorld.WORLD_SIZE_X;
                const z = Math.floor(i / VoxelWorld.WORLD_SIZE_X) % VoxelWorld.WORLD_SIZE_Z;
                const y = Math.floor(i / (VoxelWorld.WORLD_SIZE_X * VoxelWorld.WORLD_SIZE_Z));
                
                // Calculate world position (center of voxel)
                const position = new THREE.Vector3(
                    x * VoxelWorld.VOXEL_SIZE + VoxelWorld.VOXEL_SIZE / 2,
                    y * VoxelWorld.VOXEL_SIZE + VoxelWorld.VOXEL_SIZE / 2,
                    z * VoxelWorld.VOXEL_SIZE + VoxelWorld.VOXEL_SIZE / 2
                );
                
                // Set initial color: Lush green for ground, cyber blue for bunkers
                let hexColor = (VoxelWorld.voxelData[i] === 2) ? 0x1565c0 : 0x2e7d32;
                
                const r = ((hexColor >> 16) & 0xFF) / 255.0;
                const g = ((hexColor >> 8) & 0xFF) / 255.0;
                const b = (hexColor & 0xFF) / 255.0;
                VoxelWorld.instanceColor.setXYZ(count, r, g, b);

                // Calculate matrix and set it
                const instanceMatrix = new THREE.Matrix4();
                instanceMatrix.setPosition(position.x, position.y, position.z);
                VoxelWorld.voxelMesh.setMatrixAt(count, instanceMatrix);
                count++;
            }
        }
        
        VoxelWorld.voxelMesh.count = count;
        VoxelWorld.voxelMesh.instanceMatrix.needsUpdate = true;
        VoxelWorld.voxelMesh.instanceColor.needsUpdate = true;
        console.log(`Voxel World initialized with ${VoxelWorld.voxelMesh.count} instances.`);
    }

    /**
     * Updates the color of a specific voxel instance (splat decal).
     * @param {number} instanceId - The 1-based ID of the voxel instance.
     * @param {string} hexColor - Hex color string (e.g., "#F538A0").
     */
    static updatePlayerState(state) {}

    static splatVoxel(instanceId, hexColor) {
        if (instanceId < 1 || instanceId > VoxelWorld.voxelMesh.count) {
            console.error("Invalid instance ID for splatVoxel.");
            return;
        }

        const hex = parseInt(hexColor.replace('#', ''), 16);
        const r = (hex >> 16) & 0xFF / 255;
        const g = (hex >> 8) & 0xFF / 255;
        const b = hex & 0xFF / 255;

        VoxelWorld.instanceColor.setXYZ(instanceId - 1, r, g, b);
        VoxelWorld.instanceColor.needsUpdate = true;
    }
}

export default VoxelWorld;