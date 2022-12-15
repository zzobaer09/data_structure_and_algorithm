let arr = []
let target = 10

for (let i = 0; i < 1000; i++) {
    arr.push(i)
}

let start = 0
let end = arr.length - 1


const binarySearch = (arr , start , end , target) => {

    console.log(arr.slice(start , end));
    
    if (start > end) return -1

    mid = Math.floor((start + end) / 2)

    if (arr[mid] === target) return true

    if (arr[mid] > target) return binarySearch(arr , start , mid - 1 , target)
    else return binarySearch(arr , mid + 1 , end , target)

}

console.log(binarySearch(arr , start , end , target))