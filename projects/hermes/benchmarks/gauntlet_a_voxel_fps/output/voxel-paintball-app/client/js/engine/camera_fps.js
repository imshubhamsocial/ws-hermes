import * as THREE from 'three';
import { PointerLockControls } from 'three/addons/controls/PointerLockControls.js';

const GRAVITY = -24.0;
const MOVEMENT_SPEED = 5.0;
const JUMP_VELOCITY = 8.0;

export class CameraFPS {
    constructor(camera, controls, world) {
        this.camera = camera;
        this.controls = controls;
        this.world = world;
        
        this.velocity = new THREE.Vector3(0, 0, 0);
        this.direction = new THREE.Vector3();
        this.moveDirection = new THREE.Vector3();
        
        this.isGrounded = false;
        this.canJump = true;

        controls.addEventListener('lock', () => {});
        controls.addEventListener('unlock', () => {
            this.isGrounded = false;
            this.canJump = true;
        });
    }

    update(delta) {
        if (!this.controls.isLocked) return;

        this.velocity.y += GRAVITY * delta;
        
        this.moveDirection.z = Number(this.controls.moveForward) * 1;
        this.moveDirection.x = Number(this.controls.moveRight) * 1;
        
        this.direction.z = Number(this.controls.moveForward) * -1;
        this.direction.x = Number(this.controls.moveRight);
        this.direction.normalize();

        const moveVector = new THREE.Vector3();
        moveVector.addScaledVector(this.direction, this.moveDirection.z * MOVEMENT_SPEED * delta);
        moveVector.addScaledVector(new THREE.Vector3(this.controls.getObject().translateX, 0, this.controls.getObject().translateZ), this.moveDirection.x * MOVEMENT_SPEED * delta);
        
        const nextPosition = this.controls.getObject().position.clone().add(moveVector.multiplyScalar(delta));
        
        const x = Math.floor(nextPosition.x);
        const y = Math.floor(nextPosition.y);
        const z = Math.floor(nextPosition.z);
        
        const key = `${x},${y},${z}`;
        const voxelInfo = this.world.voxelMap.get(key);
        const isSolid = voxelInfo !== undefined && (voxelInfo.color.getHex() !== 0x000000);

        if (!isSolid) {
            this.controls.getObject().position.copy(nextPosition);
        }

        const nextY = this.controls.getObject().position.y + this.velocity.y * delta;
        const nextPosY = new THREE.Vector3(this.controls.getObject().position.x, nextY, this.controls.getObject().position.z);
        
        const y_x = Math.floor(nextPosY.x);
        const y_y = Math.floor(nextPosY.y);
        const y_z = Math.floor(nextPosY.z);
        const y_key = `${y_x},${y_y},${y_z}`;
        const y_voxelInfo = this.world.voxelMap.get(y_key);
        const isSolidY = y_voxelInfo !== undefined && (y_voxelInfo.color.getHex() !== 0x000000);

        if (!isSolidY) {
            this.controls.getObject().position.y = nextY;
            this.velocity.y = GRAVITY * delta;
            this.isGrounded = false;
        } else {
            this.velocity.y = 0;
            this.controls.getObject().position.y = Math.floor(nextPosY.y);
            this.isGrounded = true;
            this.canJump = true;
        }

        if (this.controls.isLocked && this.isGrounded && this.canJump) {
            this.velocity.y = JUMP_VELOCITY;
            this.canJump = false;
        }
    }
    static updatePlayerState(state) {}
}
