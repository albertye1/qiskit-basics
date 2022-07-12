namespace Solution {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Arithmetic;

    operation Solve (unitary : (Qubit[] => Unit is Adj+Ctl)) : Int {
        using(qs = Qubit[2])
		{
			X(qs[1]);
			X(qs[0]);
			unitary(qs);
			let k = MeasureInteger(LittleEndian(qs));
			ResetAll(qs);
			if(k == 1 or k == 2)
			{
				return k;
			}
		}
		using(qs = Qubit[2])
		{
			// otherwise a=b=1.
			X(qs[0]);
			unitary(qs);
			let ans = (M(qs[0]) == One ? 0 | 3);
			ResetAll(qs);
			return ans;
		}
    }
}