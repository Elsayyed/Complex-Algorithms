function [ randomList ] = mergeSortAux(randomList, lo, hi)
    if lo < hi
        midPoint = floor((lo + hi-1) / 2);
        randomList = mergeSortAux(randomList, lo, midPoint);
        randomList = mergeSortAux(randomList, midPoint + 1, hi);
        randomList = mergeList(randomList, lo, midPoint, hi);
    end
end

