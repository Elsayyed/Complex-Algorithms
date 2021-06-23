close all
clear all
clc

loopFlag = 1;

while (loopFlag)
    [loopFlag, listSize] = checkNum();
end

% Random Array Creation 
randomList = randi(1000,1,listSize);

% Matlab Sort with Timing
%ask if this's in place or not
tic
matlabSort = sort(randomList);
endTime = toc;

fprintf('\nElapsed time for Matlab sort function: %f\n\n',endTime)
fprintf('Is the list Sorted? %s\n\n',isSorted(matlabSort,listSize))

tic
randomList = MergeSort(randomList, listSize);
endTime = toc;

fprintf('\nElapsed time for Merge Sort: %f\n\n',endTime)
fprintf('Is the list Sorted? %s\n\n',isSorted(randomList,listSize))

%%%%%%%%%%%%%%%%%%%%%%%%%% Take timings for an array of n %%%%%%%%%%%%%%%
myTiming =[];
matlabTiming=[];
values = 100:50:200000

for n=100:50:200000
    
    randomList = randi(1000,1,n);
    
    tic
    randomList = MergeSort(randomList, listSize);
    time = toc;
    
    myTiming(end+1) = time;
    
    tic
    matlabSort = sort(randomList);
    time = toc;
   
    matlabTiming(end+1) = time;
end

%%%%%%%%%%%%%%%%%%%%%%%%%%%plot%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
subplot(2,1,1)
stem(values,myTiming)
xlabel("values of N")
ylabel("Timing for my method")

subplot(2,1,2)
stem(values,matlabTiming)
xlabel("values of N")
ylabel("timings for MATLAB")
