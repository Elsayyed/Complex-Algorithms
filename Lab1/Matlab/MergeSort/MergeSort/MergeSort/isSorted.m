function [loopFlag] = isSorted(inputArray, listSize)
    loopFlag = 'False';
    
    for i = 1:listSize-1
        if inputArray(i) > inputArray(i+1)
            return
        end
    end
    
    loopFlag = 'True';
end

