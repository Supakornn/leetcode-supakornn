function reverse(x: number): number {
    if(x === 0) {
        return 0
    }

    let arr = x.toString().split("");
    let isMinus = false;

    if (arr[0] === "-") {
        isMinus = true;
        arr.shift()
    }

    arr = arr.reverse()
    if (isMinus) {
        arr.unshift("-")
    }
    
    if(arr[0] === "0") {
        arr.shift()
    }

    let res = parseInt(arr.join(""))  
    if (res > Math.pow(2, 31) - 1 || res < Math.pow(-2, 31)){
        return 0
    }

    return res
};


console.log(reverse(123)); // 321
