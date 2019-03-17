# 16-Bit-MIPS-CPU-CSE332


# Instruction Formats

|Name        	   | Bit fields     |  |       |         |                   |         Notes                      |
| ---          	   | ---        | ---   |  ---    | ---               | ---    |      ----------                  |
|	           | 4 Bits     |3 Bits	| 3 Bits  | 3 Bits            | 3 Bits |                                  |
|R - Format	   | Op	        | rs	| rt	  |  rd               | funct  |   Arithmetic, Logic instruction  |
|I - Format	   | Op         | rs	| rt      | Immediate (6 Bits)|	       |   Load, Store, Branch, Immediate |



# Opcodes

|Operation        |	Opcode |  funct |	Format | Type       |	Assembly Format  |	Action        |
| -------        | ------- | ------ |-------   | -------    |   ------------     |      -------   |
|ADD(Addition)    | 0000    |  000   | R-format | Arithmetic |	add $1, $2 ,$3   |	$1 = $2 + $3  |
|SUB(Subtraction) |	0000   |  001   | R-format | Arithmetic |	sub $1, $2, $3   |	$1 = $2 - $3  |
