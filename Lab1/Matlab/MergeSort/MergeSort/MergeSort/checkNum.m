
function [loopFlag, userInputReturn] = checkNum()
    loopFlag = 1;
    userInputReturn = input('Enter the size of the array/list: ');
    if isnumeric(userInputReturn)
        loopFlag = 0;
    end
end