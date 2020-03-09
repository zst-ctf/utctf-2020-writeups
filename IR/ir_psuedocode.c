
// https://llvm.org/docs/LangRef.html
// https://idea.popcount.org/2013-07-24-ir-is-better-than-assembly/

@check = dso_local global [64 x i8] c"\03\12\1A\17\0A\EC\F2\14\0E\05\03\1D\19\0E\02\0A\1F\07\0C\01\17\06\0C\0A\19\13\0A\16\1C\18\08\07\1A\03\1D\1C\11\0B\F3\87\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\00\05", align 16, !dbg !0
@MAX_SIZE = dso_local global i32 64, align 4, !dbg !8


void _Z7reversePc(int8_t * i0) {
    int32_t i2; // alloca
    int8_t * i3; // alloca
    int32_t i4; // alloca
    int32_t i5; // alloca
    int32_t i6; // alloca

    i3 = i0; // store

    i4 = 0; // store

    goto label7; // br label

label7:
	i8 = &i4; // load
	i9 = &MAX_SIZE; // load
	i10 = i8 < i9; // icmp slt

	if (i10)
		goto label11;
	else
		goto label23;

label11:
	i15 = i3[i4] //getelementptr
	i15 = i15 + 5; // add nsw
	goto label20;

label20:
	i4 += 1; // add nsw
	goto label7;

label23:
	i5 = 0; // store
	goto label24;

label24:
	if (i5 < MAX_SIZE-1)
		goto label29;
	else
		goto label48;

label29:
	i34 = i3[i5+1] //getelementptr
	i40 = i3[i5] //getelementptr

	i43 = i34 ^ i40; // xor
	i40 = i43;

	goto label45;

label45:
	i5 += 1;
	goto label24;

label48:
	i6 = 0;
	goto label49;

label49:
	if (i6 < MAX_SIZE)
		goto label53;
	else
		goto label71;

label53:
	i55 = i6
	i58 = (check)[i6]; // getelementptr

	i64 = i3[i6]; // getelementptr

	if (i58 != i64) {
		goto label66;
	} else {
		goto label67;
	}

label66:
	i2 = 0; // store
	goto label72;

label67:
	goto label68;

label68:
	i6 += 1;
	goto label49;

label71:
	i2 = 1; // store
	goto label72;

label72:
	return i2;
}

// Input a string to the function
// The function will add 5 to each character
// Then xor each pair of chars.
// Finally, it will run a check against the output
