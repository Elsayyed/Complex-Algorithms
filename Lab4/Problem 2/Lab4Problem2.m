% % clc
% % clear all
% % 
% % matrixDim = input('Please input the dimension of the NxN matrix: ')
% % A = randi(100,matrixDim)
% % T_Matlab = zeros(1,5); %Timing for the 5 different b' values.
% % T_Our = zeros(1,5); %Timing for the 5 different b' values.
% % DecompTimeMat = 0;
% % DecompTimeOur = 0;
% % 
% % tic;
% % [L, U] = lu(sparse(A), 0); %try to change this without sparse.
% % DecompTimeMat = toc;
% % 
% % tic;
% % lu_us = LUDecomposition(A);
% % DecompTimeOur = toc;
% % 
% % for i=1:5
% %     b = randi(100,[matrixDim,1]);
% %     tic;
% %     A_Matlab = mldivide(A,b);
% %     T_Matlab(i) = toc;
% %     tic;
% %     A_OurSolution = LUSolve(lu_us,b);
% %     T_Our(i) = toc;
% % %   A_Matlab = round(A_Matlab,4); 
% % %   Norm of a matrix to get the error dif. Norm()
% % %   A_OurSolution = round(A_OurSolution,4);
% % %   Justifying with a percentage of error.
% %     x = isequal(A_Matlab,A_OurSolution);
% %     fprintf('The solution is equal: %d \n', x)
% % end
% % 
% % % 
% % % 
% % % n = 1:25:500
% % % [r,c] = size(n)
% % % 
% % % DecompTimeMat = zeros(1,c);
% % % DecompTimeOur = zeros(1,c);
% % % 
% % % for i=1:c
% % %     A = randi(100,n(i));
% % %     b = randi(100,[n(i),1]);
% % %     
% % %     tic;
% % %     [L, U] = lu(sparse(A), 0);
% % %     DecompTimeMat(i) = toc;
% % % 
% % %     tic;
% % %     lu_us = LUDecomposition(A);
% % %     DecompTimeOur(i) = toc;
% % % 
% % %     tic;
% % %     A_Matlab = mldivide(A,b);
% % %     T_Matlab(i) = toc;
% % %     tic;
% % %     A_OurSolution = LUSolve(lu_us,b);
% % %     T_Our(i) = toc;
% % % end
% % % 
% % % figure(1)
% % % title('LU Decomposition Timing')
% % % subplot(1,2,1)
% % % plot(n,DecompTimeMat)
% % % 
% % % subplot(1,2,2)
% % % plot(n,DecompTimeOur)
% % % xlabel('n')
% % % ylabel('Time')
% % % title('LU Decomposition Timing')
% % % sgtitle('TEST')
% % 

%%%%%%%%%%%%%%%%%%%%%%NEW VERSIONNNNN WITH PLOTS%%%%%%%%%%%%%

clc
clear all

matrixDim = input('Please input the dimension of the NxN matrix: ');
A = randi(100,matrixDim);
T_Matlab = zeros(1,5); %Timing for the 5 different b' values.
T_Our = zeros(1,5); %Timing for the 5 different b' values.
DecompTimeMat = 0;
DecompTimeOur = 0;


%MATLAB BUILT IN FUNCTION TESTING:
tic;
[L, U] = lu(A);
DecompTimeMat = toc;
A_MATLAB = L*U; %Try to get the original array back from the L and U caluclated using MATLAB
MATLAB_error = norm(A - A_MATLAB);  %try to see the value of error in the regained A using MATLAB

%OUR FUNCTION TESTING 
tic;
lu_us = LUDecomposition(A);
DecompTimeOur = toc;

L_us =tril(lu_us); %gives the lower triangle of calculate lu which is (L)

for i=1:matrixDim
    for j=0:matrixDim
        if(i==j)
            L_us(i,j)=1; %replacing the diagonal of the lower trinagle with ones so we have 1  0  0
            %                                                                               A1 1  0
            %                                                                               A2 A3 1
        end
    end
end
U_us = triu(lu_us); %Giving the upper triangle of the calculated lu which is (U)

A_us = L_us*U_us; %getting the original array back from the calculated U and L
US_error = norm(A - A_us); %calculating the error 

fprintf("MATLAB error is %d\n",MATLAB_error);
fprintf("Our impementation error is %d\n",MATLAB_error);


%Solving the linear equation for 5 different right hand sides
for i=1:5
    b = randi(100,[matrixDim,1]);
    tic;
    A_Matlab = mldivide(A,b);
    T_Matlab(i) = toc;
    tic;
    A_OurSolution = LUSolve(lu_us,b);
    T_Our(i) = toc;
end

%Solving for different sizes of m
n = 100:100:2000;
[r,c] = size(n);

DecompTimeMat = zeros(1,c);
DecompTimeOur = zeros(1,c);

for i=1:c
    n(i)
    A = randi(100,n(i));
    b = randi(100,[n(i),1]);
    
    tic;
    [L, U] = lu(A);
    DecompTimeMat(i) = toc;

    tic;
    lu_us = LUDecomposition(A);
    DecompTimeOur(i) = toc;

    tic;
    A_Matlab = mldivide(A,b);
    T_Matlab(i) = toc;
    tic;
    A_OurSolution = LUSolve(lu_us,b);
    T_Our(i) = toc;
end
%Variables needed for comparing the values to theoretocal timings
eliminitation_expectation = n.^3;
substitution_expectation = n.^2;

elminFactorMatlab = DecompTimeMat(end)/eliminitation_expectation(end);
elimFactorUs =  mean(DecompTimeOur./eliminitation_expectation);
subFactorMatlab = mean(T_Matlab./substitution_expectation);
subFactorUs = T_Our(end)/substitution_expectation(end);

%Plotting

%Elimination 
figure(1)
subplot(1,2,1)
plot(n,DecompTimeMat)
hold on
plot(n,elminFactorMatlab.*eliminitation_expectation)
title('LU Decomposition Timing MATLAB')
xlabel('n')
ylabel('Time')
legend(["Tested" sprintf('%1.4e* theoretical',elminFactorMatlab)])

subplot(1,2,2)
plot(n,DecompTimeOur)
hold on
plot(n,elimFactorUs.*eliminitation_expectation)
xlabel('n')
ylabel('Time')
title('LU Decomposition Timing our implementation')
legend(["Tested" sprintf('%1.4e* theoretical',elimFactorUs)])

%Substitution 
figure(2)
subplot(1,2,1)
plot(n,T_Matlab)
hold on
plot(n,subFactorMatlab*substitution_expectation)
title('Substitution Timing MATLAB')
xlabel('n')
ylabel('Time')
legend(["Tested" sprintf('%1.4e* theoretical',subFactorMatlab)])


subplot(1,2,2)
plot(n,T_Our)
hold on
plot(n,subFactorUs*substitution_expectation)
xlabel('n')
ylabel('Time')
title('Substitution Timing our implementation')
legend(["Tested" sprintf('%1.4e* theoretical',subFactorUs)])

