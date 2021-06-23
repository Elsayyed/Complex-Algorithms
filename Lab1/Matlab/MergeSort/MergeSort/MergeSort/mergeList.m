function [ A ] = mergeList(A, p, q, r)
    
    left = q - p + 1;
    right = r - q;

    L = zeros(1,left+1) ;
    R = zeros(1,right+1);

    for i=1:left
        L(i) = A(p + i -1);
    end
    
    for j=1:right
        R(j) = A(q + j);
    end
    
    L(left+1) = inf;
    R(right+1) = inf;

    i = 1;
    j = 1;

    for k=p:r
        if L(i) <= R(j)
            A(k) = L(i);
            i = i + 1;
        else
            A(k) = R(j);
            j = j + 1;
        end
    end
    
end

