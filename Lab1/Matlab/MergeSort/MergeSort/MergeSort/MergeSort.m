function [randomList] = MergeSort( randomList, listSize )
    randomList = mergeSortAux(randomList, 1, listSize);
    
end

