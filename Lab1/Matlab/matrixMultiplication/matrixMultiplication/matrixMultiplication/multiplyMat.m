function [C] = multiplyMat(A,B)
    sizeA = size(A);
    sizeB = size(B);
    m = sizeA(1);
    p = sizeA(2);
    n = sizeB(2);
    C = zeros(m,n);
    for i=1:m
        for j=1:n 
            C(i,j) = 0;
            for k=1:p
                C(i,j) = C(i,j) + A(i,k)*B(k,j);
            end
        end
    end
end

