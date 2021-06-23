function [x] = LUSolve(A,b)
    d = 0*b; %where b is the svec (RHS)
    dim = size(A);
    n = dim(2);
    for i=1:n
        d(i)=b(i);
        for j=1:i-1
            d(i)=d(i)-A(i,j)*d(j);
        end
        d(i)=d(i)/1;
    end
    x = 0*d; %where x is a svec
    for i=n:-1:1
        x(i)=d(i);
        for j=i+1:n
            x(i)=x(i)-A(i,j).*x(j);
        end
        x(i)=x(i)/A(i,i);
    end
end