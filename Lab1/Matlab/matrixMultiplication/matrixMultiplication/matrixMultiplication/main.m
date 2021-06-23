clear all
clc

rowA = 0;
rowB = 0;
colA = 0;
colB = 0;
loop=1;
while loop
    rowA = input('Enter the Number of Rows in A: ');
    colA = input('Enter the Number of Columns in A: ');
    rowB = input('Enter the Number of Rows in B: ');
    colB = input('Enter the Number of Columns in B: ');
    if(colA == rowB)
        break 
    end
        display("WRONG INPUT!TRY AGAIN")
end
%%%%%%%%%%%%%%%%% Make random sample of input %%%%%%%%%%%%%%%%%%%
A = randi(30,rowA,colA);
B = randi(30,rowB,colB);
%%%%%%%%%%%%%%%%%%% My method %%%%%%%%%%%%%%%%
disp('The result of the matrix multiplication')
tic
AB = multiplyMat(A,B)
time=toc
fprintf("The elapsed time for my method is: %f\n",time)
%%%%%%%%%%%%%%%%%%%%%%%%%% Matlab Calculations %%%%%%%%%%%%%%%%%%%%%%%%
disp('The result of the matrix multiplication')
tic
productMATLAB = A*B
time=toc
fprintf("The elapsed time for MATLAB is: %f",time)
fprintf('\nare the two arrays are equal?')
truth = isequal(AB,productMATLAB);
fprintf(log2str(truth));
%%%%%%%%%%%%%%%%%%%%%%%%%% Take timings for an array of n %%%%%%%%%%%%%%%
myTiming =[];
matlabTiming=[];
values = 100:10:600;
for n=100:10:600
    A = randi(30,n,n);
    B = randi(30,n,n);
    tic
    AB = multiplyMat(A,B);
    time=toc;
    myTiming(end+1) = time;
    tic
    AB = multiplyMat(A,B);
    time=toc;
    matlabTiming(end+1) = time;
end
%%%%%%%%%%%%%%%%%%%%%%%%%%%plot%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
subplot(2,1,1)
plot(values,myTiming)
xlabel("values of N")
ylabel("Timing for my method")

subplot(2,1,2)
plot(values,matlabTiming)
xlabel("values of N")
ylabel("timings for MATLAB")