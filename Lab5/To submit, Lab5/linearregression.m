function [r2 c x] = linearregression(dataSet)

A = dataSet(:,1:end-1); 
b = dataSet(:,end);  

x = (A'*A)\(A'*b)

dim = size(x)
length = dim(1) %get the column

dim2 = size(b)
length2 = dim2(1)

c = zeros(length2,1);

average_mark = mean(b);
St = sum((b-average_mark).^2);

c = c + x(1);

%make our X = [1 2 3] how the line looks like %r2 = 1%error 
%Determine Sr:
for i=2:length
    c = c + x(i)*A(:,i);
end

Sr = sum((b-c).^2);

r2 = (St - Sr)./St;
end

