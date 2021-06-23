clc
clear
close all

marks = [45 53 58 60 60 61 63 65 65, 67, 68 68 69 70 72 72 73 74 74 74 74 75 75 75 76 79 79 ...
80, 82, 82, 83, 84 85, 86, 88, 89, 92, 95, 95, 98].'; 

studyhours = 0.5*[1 1 3 0.5 1 1 2 2 1 2 3 3 3 4 3 4 6 3 4 4 4 3 5 5 5 4 5 6 6 5 6 7 8 5 4 8 4 9 9 6].';

credithours = [18 20 25 24 30 32 25 28 20 19 44 30 37 33 40 45 50 56 80 65 70 75 79 84 55 70 90 94 93 110 105 120 140 133 154 160 50 135 120 140].';

n = length(marks);

%create data set 
inputDataSet = [ones(n,1) credithours marks]
[r2,c,coeffA] = linearregression(inputDataSet)

figure;
scatter(credithours, marks)
hold on
plot(credithours,c)

