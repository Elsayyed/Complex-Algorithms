close all
clear all
clc

marks = [45 53 58 60 60 61 63 65 65, 67, 68 68 69 70 72 72 73 74 74 74 74 75 75 75 76 79 79 ...
80, 82, 82, 83, 84 85, 86, 88, 89, 92, 95, 95, 98].'; 

studyhours = 0.5*[1 1 3 0.5 1 1 2 2 1 2 3 3 3 4 3 4 6 3 4 4 4 3 5 5 5 4 5 6 6 5 6 7 8 5 4 8 4 9 9 6].';

credithours = [18 20 25 24 30 32 25 28 20 19 44 30 37 33 40 45 50 56 80 65 70 75 79 84 55 70 90 94 93 110 105 120 140 133 154 160 50 135 120 140].';

n = length(marks);
assert(n == length(studyhours));
assert(n == length(credithours));

%construct the over-determined system of equations
A = [ones(n,1) studyhours credithours];
b = marks;

%solve the over-determined system
x = (A'*A)\(A'*b); %these are the coefficients for the line - better is A\b directly
a0 = x(1);
a1 = x(2);
a2 = x(3);

%determine R^2
average_mark = mean(marks);
St = sum((marks-average_mark).^2);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
testttt= x(2)*studyhours
Sr = sum((marks-(x(1) + x(2)*studyhours + x(3)*credithours)).^2)

r2 = (St - Sr)./St

%correlation coefficients (returns r not r^2)
%corrcoef(marks, x(1) + x(2)*study_hours + x(3)*credit_hours) 

fh = @(x,y) a0 + a1*x + a2*y; %function handle for ezmesh and fmesh

figure;
%ezmesh(fh); %old matlab way but scatter3 won't work over this (?)
fmesh(fh, [min(studyhours), max(studyhours), min(credithours), max(credithours)]); %new matlab way
hold on
scatter3(studyhours, credithours, marks)
title('Professor Xs Midterm Marks', 'FontSize', 18)
xlabel('Average Hours Per Week', 'FontSize', 14)
ylabel('Total Credit Hours Completed', 'FontSize', 14)
zlabel('Marks', 'FontSize', 14)
legend({'data', ['regression fit with r-sqr = ' num2str(r2*100) '%']}, 'FontSize', 14)


