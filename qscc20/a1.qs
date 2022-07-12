namespace Solution {
    open Microsoft.Quantum.Intrinsic;

    operation Solve (unitary : (Qubit[] => Unit is Adj+Ctl)) : Int {
        // your code here
		using(qs = Qubit[2])
		{
			X(qs[0]);
			unitary(qs);
			let ans = (M(qs[1]) == One ? 0 | 1);
			ResetAll(qs);
			return ans;
		}
    }
}