ObjectRotate:
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x288
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x90
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x18D
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x13C
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0xDE
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0xE0
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0xE1
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0xDD
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0xDF
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x48
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x28F
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x5B
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x1F2
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x1F3
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x1F5
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x1F6
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x59
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x257
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x258
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x259
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x25A
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x25B
    beq $v0, $at, ObjectRotate_ApplyRotate
    addiu $at, $zero, 0x25C
    beq $v0, $at, ObjectRotate_ApplyRotate
    nop
    j 0x80637150
    nop

    ObjectRotate_ApplyRotate:
        j 0x80637160
        nop