facto(0,1).
facto(X,Y):- E is X-1,facto(E,Y2),Y is X*Y2.
