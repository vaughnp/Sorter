/*
 * Merges two arrays in order based on their natural
 * relationship.
 * @param {Array} left The first array to merge.
 * @param {Array} right The second array to merge.
 * @return {Array} The merged array.
 */
var flag = 0

function textUpdater(left, right){
    left
    //return ()
}

function merge(left, right){
    var result  = [],
        il      = 0,
        ir      = 0;

    while (il < left.length && ir < right.length){
    flag = prompt("Which is better, " + left[il] + " or " + right[ir] + "? Put 1 for left and 2 for right.");
    //flag = textUpdater(left[il], right[ir]);

        if (flag == 1){
            result.push(left[il++]);
        } 
        else {
            result.push(right[ir++]);
        }
    }

    return result.concat(left.slice(il)).concat(right.slice(ir));
}

/**
 * Sorts an array in ascending natural order using
 * merge sort.
 * @param {Array} items The array to sort.
 * @return {Array} The sorted array.
 */
function mergeSort(items){

    if (items.length < 2) {
        return items;
    }

    var middle = Math.floor(items.length / 2),
        left    = items.slice(0, middle),
        right   = items.slice(middle);

    return merge(mergeSort(left), mergeSort(right));
}

var array = ["Facebook", "Donuts", "Twitter", "Snow", "Homework"]
window.alert(mergeSort(array))