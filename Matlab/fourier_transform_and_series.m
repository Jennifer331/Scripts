syms t;
f = exp(j*t)*sign(sin(t));
f = matlabFunction(f);
integral(f, -pi, pi)
f1 = exp(-j*t)*sign(sin(t));
f1 = matlabFunction(f1);
integral(f1, -pi, pi)