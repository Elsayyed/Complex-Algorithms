clc
clear all
close all

x = [1:1:10].'; 

a1 = 2
a0 = 20
y = a0 + a1*x

randomArray = round(-5 + (10+(5)).*rand(length(x),1));
yNoisy = a0 + a1*x + randomArray

n = length(x);
%create data set
inputDataSet = [ones(n,1) x y]
[r2,c,coeffA] = linearregression(inputDataSet)

if (a0 == round(coeffA(1)) && a1 == round(coeffA(2)) )
    ansStr = 'true'
else
    ansStr = 'false'
end

fprintf('Does the values of coefficient match: %s\n', ansStr)
assert(r2 == 1,'the correlation coefficient is NOT equal to 1')

%create Noisy data set 
inputDataSet = [ones(n,1) x yNoisy]
[r2,cNoisy,coeffA_Noisy] = linearregression(inputDataSet)

figure;
scatter(x, y)
hold on
plot(x,c)

figure;
scatter(x, yNoisy)
hold on
plot(x,cNoisy)
legend(["Original data",sprintf('approximated r^2 = %f',r2)])


