/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    let transformedArray = []
    for (let i=0; i< arr.length; i++){
        transformedArray.push(fn(arr[i], i))
    }
    return transformedArray
    
};

// more efficient way:
var map = function(arr, fn){
    let result = new Array(arr.length)
    for (let i = 0 ; i < arr.length; i++){
        result[i] = (fn(arr[i],i))
    }
    return result
}