function [A] = LUDecomposition(A)
    dim = size(A);
    n = dim(2);
    for j=1:n-1
        if A(j,j)==0
            msg = 'Pivot element is a zero, can not handle!';
            error(msg)
        end
        for i=j+1:n
            L = A(i,j)/A(j,j);
            A(i,j) = L;
%             for k=j+1:n
%                 U =A(i,k)-L*A(j,k)
%                 A(i,k) = U 
%             end
            A(i,j+1:n) = A(i,j+1:n)-L*A(j,j+1:n);
        end
    end
end
